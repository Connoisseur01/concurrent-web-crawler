import requests
from bs4 import BeautifulSoup
import threading

class Scraper(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # Get the HTML content of the URL
        response = requests.get(self.url)
        html = response.content

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Find all the links on the page and print them
        for link in soup.find_all('a'):
            print(link.get('href'))