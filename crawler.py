import threading
import requests
from bs4 import BeautifulSoup

class Crawler(threading.Thread):
    def __init__(self, pages, links, locks):
        threading.Thread.__init__(self)
        self.pages = pages
        self.links = links
        self.locks = locks

    def run(self):
        while len(self.pages) > 0:
            with self.locks[0]:
                url = self.pages.pop(0)
            # Make a GET request to the website
            response = requests.get(url, timeout=10)
            # Parse the HTML content using Beautiful Soup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the links on the page and print them
            for link in \
                soup.find_all(class_='woocommerce-LoopProduct-link woocommerce-loop-product__link'):
                
                with self.locks[1]:
                    self.links.append(link.get('href'))

