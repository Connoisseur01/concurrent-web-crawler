import threading
import requests
from bs4 import BeautifulSoup

class Scraper(threading.Thread):
    """
    parse html from product links to extract and save relevant data

    Attributes
    ----------
    links : list
        individual product pages links
    locks : list
        list of locks
    data : list
        list where scraped data is saved

    Methods
    -------
    start():
        starts a thread by calling the run method
    """
    def __init__(self, links, lock, data):
        threading.Thread.__init__(self)
        self.links = links
        self.lock = lock
        self.data = data

    def run(self):
        while len(self.links) > 0:
            with self.lock:
                link = self.links.pop(0)
            # Make a GET request to the website
            response = requests.get(link, timeout=10)
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the relevant information on the page
            product_name = soup.find("h1", class_="product_title").text
            product_price = soup.find("span", class_="price").text
            product_description = \
            soup.find("div", class_="woocommerce-product-details__short-description").text.strip()
            stock = soup.find("p", class_ = "stock").text

            # save information to data list
            self.data.append([product_name, product_price, product_description, stock])
            print(product_name, product_price, stock)
