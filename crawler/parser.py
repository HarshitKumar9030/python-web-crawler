from bs4 import BeautifulSoup

from crawler.constants import USELESS_KEYWORDS


def parse_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = {
        "text": [],
        "code_blocks": [],
        "important_text": []
    }

    for code_block in soup.find_all('pre'):
        data["code_blocks"].append(code_block.get_text())

    for strong in soup.find_all(['strong', 'h1', 'h2', 'h3', 'li', 'p']):
        data["important_text"].append(strong.get_text())

    for tag in soup.find_all(['p', 'span', 'div']):
        text = tag.get_text(strip=True)
        if text and not is_useless_text(text):
            data["text"].append(text)

    return data


def is_useless_text(text):
    useless_keywords = ['advertisement', 'cookies', 'subscribe']
    return any(keyword in text.lower() for keyword in USELESS_KEYWORDS)
