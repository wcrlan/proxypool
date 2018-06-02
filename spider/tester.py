import time
import urllib3
import requests
from db import db

from setting import HEADERS, TEST_URL


def valid(proxy):
    print('test proxy %s' % proxy)
    proxies = {'http': 'http://%s' % proxy, 'https': 'https://%s' % proxy}
    try:
        start = time.time()
        urllib3.disable_warnings()
        resp = requests.get(TEST_URL, proxies=proxies, headers=HEADERS, verify=False)
        if resp.status_code in [200, 302]:
            delay = round(time.time() - start)
            print('update %s by delay %s' % (proxies, delay))
            db.update({'address': proxy}, {'delay': delay})
        else:
            print('验证请求错误!', proxy)
    except Exception:
        pass
