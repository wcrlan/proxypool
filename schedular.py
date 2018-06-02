import time
from multiprocessing import Process
from multiprocessing.pool import ThreadPool

from db import db
from setting import RULES, PORT
from spider import crawl_2_db, valid
from api import api_process


def fetch_process():
    while True:
        print('start fetch proxy......')
        for rule in RULES:
            crawl_2_db(rule)
        time.sleep(30*60)


def test_process():
    pool = ThreadPool(10)
    pool.map(valid, db.all())


def run():

    p1 = Process(target=fetch_process)
    p2 = Process(target=test_process)
    p3 = Process(target=api_process, args=(PORT,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
    run()
