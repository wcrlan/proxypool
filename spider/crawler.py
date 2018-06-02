from .getter import getter
from db.mongo_db import db


def crawl_2_db(rule):
    for resp in getter.fetch(rule):
        for ip_port in getter.parse(resp, rule):
            proxy = {'address': ip_port, 'delay': -1}
            db.insert(proxy)
