import threading
from queue import Queue
#from typing_extensions import TypeVarTuple
from class_spider import spider
from class_domain import *
from general import *

PROJECT_NAME = input("[+] Enter Project Name :")
HOMEPAGE = input("[+] Enter URL to Crawl :")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = 'E:\projects\web Crawler' +extend+ PROJECT_NAME + extend +'queue.txt'
CRAWLED_FILE ='E:\projects\web Crawler'+ extend + PROJECT_NAME + extend + 'crawled.txt'
NUMBER_OF_THREADS = int(input("[+] Enter no. of threads (type '5' for default): "))

queue = Queue()
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def create_work():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_work()

create_spiders()
crawl()