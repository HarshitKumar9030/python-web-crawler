import requests
import threading
from time import sleep
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from crawler.parser import parse_content
from crawler.storage import save_data
from crawler.utils import handle_error, apply_rate_limit
from crawler.config_loader import load_config
from tqdm import tqdm


class WebCrawler:
    def __init__(self, websites, output_type, output_path, rate_limit):
        self.websites = websites
        self.output_type = output_type
        self.output_path = output_path
        self.rate_limit = rate_limit
        self.session = requests.Session()
        self.visited_urls = set()
        self.pages_to_crawl = []
        self.progress_bar = None
        self.lock = threading.Lock()

    def fetch_page(self, url):
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            handle_error(e, url)
            return None

    def crawl(self):
        self.progress_bar = tqdm(total=1, desc="Crawling pages", unit="page")
        threading.Thread(target=self.estimate_total_pages).start()

        for website in self.websites:
            self.recursive_crawl(website)
        
        self.progress_bar.close()

    def recursive_crawl(self, url):
        if url in self.visited_urls:
            return

        self.visited_urls.add(url)
        self.pages_to_crawl.append(url)
        content = self.fetch_page(url)
        
        if not content:
            return

        parsed_data = parse_content(content)
        save_data(parsed_data, self.output_type, self.output_path)

        soup = BeautifulSoup(content, 'html.parser')
        base_url = "{0.scheme}://{0.netloc}".format(urlparse(url))
        new_links = []
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            full_url = urljoin(base_url, href)
            if self.is_internal_link(full_url, base_url):
                new_links.append(full_url)

        with self.lock:
            self.pages_to_crawl.extend(new_links)
            self.progress_bar.total = len(self.pages_to_crawl)
            self.progress_bar.update(1)

        for new_url in new_links:
            self.recursive_crawl(new_url)

        apply_rate_limit(self.rate_limit)

    def is_internal_link(self, url, base_url):
        """Checks if a URL is an internal link of the base domain."""
        return url.startswith(base_url) and url not in self.visited_urls

    def estimate_total_pages(self):
        """Thread function to monitor the total pages count dynamically."""
        while True:
            with self.lock:
                self.progress_bar.total = len(self.pages_to_crawl)
            if self.progress_bar.n >= self.progress_bar.total:
                break


if __name__ == "__main__":
    config = load_config("config/config.yaml")
    crawler = WebCrawler(config["websites"], config["output"]["type"], config["output"]["path"], config["rate_limit"])
    crawler.crawl()
