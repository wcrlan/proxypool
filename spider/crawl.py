
from multiprocessing.pool import ThreadPool

from .getter import getter

from db import db

def crawl(rule):
    for resp in getter.fetch(rule):
        for ip_port in getter.parse(resp, rule):
            proxy = {'address': ip_port, 'delay': -1}
            db.insert(proxy)


def crawl_many(rules, crawl_thread_num):
    pool = ThreadPool(crawl_thread_num)
    pool.map(crawl, rules)
