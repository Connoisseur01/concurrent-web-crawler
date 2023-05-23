import time
import csv
from threading import Lock
from crawler import Crawler
from scraper import Scraper


URL = 'https://scrapeme.live/shop/'
PAGES_NUM = 10
CRAWLER_NUM = 3
SCRAPER_NUM = 3


def run_threading():
    """Function running web crawlers and scrapers concurrently."""
    # Create a list of pages
    pages = []
    pages.append(URL)
    for i in range(2, PAGES_NUM+1):
        page = URL + 'page/' + str(i) + '/'
        pages.append(page)

    # create a list of threads
    threads = []
    # create a list of links to scrape
    links = []
    # create mutex locks
    page_lock = Lock()
    link_lock = Lock()
    locks = [page_lock, link_lock]

    # Start all the crawler threads
    for i in range(CRAWLER_NUM):
        thread = Crawler(pages, links, locks)
        thread.start()
        threads.append(thread)

    time.sleep(1)
    # create a list for scraped data
    data = [["name", "price", "description", "stock"]]

    # Start all the scraper threads
    for i in range(SCRAPER_NUM):
        thread = Scraper(links, locks[1], data)
        thread.start()
        threads.append(thread)
    
    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    # Save the data in a CSV file
    with open("pokemon.csv", "w", newline="", encoding="utf8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

if __name__ == '__main__':
    run_threading()
