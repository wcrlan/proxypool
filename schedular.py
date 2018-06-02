import time
from multiprocessing import Process
from multiprocessing.pool import ThreadPool

from db import db
from setting import RULES, API_PORT, API_HOST, VALID_CYCLE, CRAWL_CYCLE, VALID_RUN, CRAWL_RUN, API_RUN, CRAWL_THREAD_NUM
from spider import crawl_many, valid_many
from api import app


class Scheduler(object):

    def crawl_server(self, rules=RULES, crawl_thread_num=CRAWL_THREAD_NUM, cycle=CRAWL_CYCLE):
        while True:
            print('start fetch proxy......')
            crawl_many(rules, crawl_thread_num)
            time.sleep(cycle)

    def valid_server(self, cycle=VALID_CYCLE):
        while True:
            proxy_list = db.all()
            valid_many(proxy_list)
            time.sleep(cycle)

    def api_server(self, host, port):
        app.run(host=host, port=port)

    def run(self):
        print('代理池开始运行')
        if VALID_RUN:
            valid_process = Process(target=self.valid_server)
            valid_process.start()

        if CRAWL_RUN:
            crawl_process = Process(target=self.crawl_server)
            crawl_process.start()

        if API_RUN:
            api_process = Process(target=self.api_server, args=(API_HOST, API_PORT))
            api_process.start()

