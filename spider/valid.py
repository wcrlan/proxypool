import time
from multiprocessing.pool import ThreadPool

import requests
import urllib3

from db import db
from setting import VALID_THREAD_NUM, VALID_URL


def valid(proxy):
    print('test proxy %s' % proxy)
    proxies = {'http': 'http://%s' % proxy, 'https': 'https://%s' % proxy}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/66.0.3359.181 Safari/537.36'}
    try:
        start = time.time()
        urllib3.disable_warnings()
        resp = requests.get(VALID_URL, proxies=proxies,
                            headers=headers, verify=False)
        if resp.status_code in [200, 302]:
            delay = round(time.time() - start)
            print('update %s by delay %s' % (proxies, delay))
            db.update({'address': proxy}, {'delay': delay})
        else:
            print('验证请求错误!', proxy)
    except Exception:
        pass


def valid_many(proxy_list):
    pool = ThreadPool(VALID_THREAD_NUM)
    pool.map(valid, proxy_list)
