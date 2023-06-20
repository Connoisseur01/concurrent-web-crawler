import time
import csv
from threading import Lock
from crawler import Crawler
from scraper import Scraper


URL = 'https://scrapeme.live/shop/'


def run_threading(pages_num, crawlers_num, scrapers_num, filename):
    """Function running web crawlers and scrapers concurrently."""
    # Create a list of pages and links shared between threads
    pages = []
    links = []

    pages.append(URL)
    for i in range(2, pages_num+1):
        page = URL + 'page/' + str(i) + '/'
        pages.append(page)

    # create a list of threads
    threads = []

    # create mutex locks for respective lists
    page_lock = Lock()
    link_lock = Lock()
    locks = [page_lock, link_lock]

    # Start all the crawler threads
    for i in range(crawlers_num):
        thread = Crawler(pages, links, locks)
        thread.start()
        threads.append(thread)

    # wait so that the list of pages is not empty
    time.sleep(1)
    # create a list for scraped data
    data = [["name", "price", "description", "stock"]]

    # Start all the scraper threads
    for i in range(scrapers_num):
        thread = Scraper(links, locks[1], data)
        thread.start()
        threads.append(thread)

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    # Save the data in a CSV file
    with open(filename, "w", newline="", encoding="utf8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

if __name__ == '__main__':

    pages_num = int(input("number of subpages to scrape: "))
    crawlers_num = int(input("number of crawler threads: "))
    scrapers_num = int(input("number of scraper threads: "))
    filename = input("file name: ")

    start = time.time()
    run_threading(pages_num, crawlers_num, scrapers_num, filename)
    end = time.time()
    elapsed = end - start
    print(f"\nscraping complited in {elapsed:.2f} seconds")
