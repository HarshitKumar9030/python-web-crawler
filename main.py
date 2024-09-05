import argparse
from crawler.crawler import WebCrawler
from crawler.utils import load_config

def main():
    parser = argparse.ArgumentParser(description='A web crawler.')
    parser.add_argument('--config', type=str, help='Path to the config file', default='config/config.yaml')
    args = parser.parse_args()

    config = load_config(args.config)
    crawler = WebCrawler(config["websites"], config["output"]["type"], config["output"]["path"], config["rate_limit"])
    crawler.crawl()

if __name__ == "__main__":
    main()
