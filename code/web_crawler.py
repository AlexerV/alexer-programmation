import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def crawl(self, url):
        self.visited_urls.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            next_url = link.get('href')
            next_url = urljoin(url, next_url)
            next_url = next_url.split('#')[0]
            if next_url not in self.visited_urls and self.is_valid_url(next_url):
                self.crawl(next_url)

if __name__ == "__main__":
    start_url = 'URL'
    crawler = WebCrawler(start_url)
    crawler.crawl(start_url)
