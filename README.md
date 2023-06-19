# concurrent-web-crawler

An example python-based web crawler that uses multithreading to concurrently crawl through https://scrapeme.live/shop/ site and scrape product information like: name, price, description etc.

### threads

**Crawlers** - Crawler threads parse html content of shop subpages and save individual product links to *link* list for scrapers.

**Scrapers** - Scraper threads parse html from product links to extract and save relevant data.

### mutexes

there are two lists that threads need to share access to:

* *pages* - stores shop subpages
* *links* - stores individual product pages links

Two mutex lock objects are created to synchronise access to these lists by threads. When a thread writes or reads data from these lists it acquires respective lock and releases it after the operation. If a thread wants to acquire a lock thats already in use it will wait for it to release.
