from Scraper import Scraper

url = 'https://scrapeme.live/shop/'
pages_num = 10

def run_threading():
    # Create a list of threads
    threads = []
    thread = Scraper(url)
    threads.append(thread)
    for i in range(2, pages_num+1):
        page = url + 'page/' + str(i) + '/'
        thread = Scraper(page)
        threads.append(thread)
 
    # Start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    run_threading()