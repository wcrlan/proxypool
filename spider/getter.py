import time
import re
import chardet
import requests
from pyquery import PyQuery as pq


class Getter(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

    def fetch(self, rule):
        for url in rule['urls']:
            try:
                print('download %s' % url)
                resp = requests.get(url, headers=self.headers, timeout=10)
                if resp.status_code == 200:
                    resp.encoding = chardet.detect(resp.content).get('encoding')
                    yield resp.text
                else:
                    raise ConnectionError
            except Exception:
                print('download %s failed' % url)
            if rule.get('delay'):
                time.sleep(rule.get('delay'))

    def parse(self, resp, rule):
        if rule['parse'] == 'css':
            return self.parse_by_css(resp, rule)
        if rule['parse'] == 're':
            return self.parse_by_re(resp, rule)
        if rule['parse'] == 'xpath':
            return self.parse_by_xpath(resp, rule)

    def parse_by_css(self, resp, rule):
        try:
            proxies = pq(resp)(rule['pattern'])
            for item in proxies.items():
                yield '{ip}:{port}'.format(
                    ip=item(rule['target']['ip']).text(),
                    port=item(rule['target']['port']).text()
                )
        except Exception as e:
            print('parse error: %s' % e)

    def parse_by_re(self, resp, rule):
        try:
            proxies = re.findall(rule['pattern'], resp, re.S)
            for item in proxies:
                yield '{ip}:{port}'.format(
                    ip=item[rule['target']['ip']],
                    port=item[rule['target']['port']]
                )
        except Exception as e:
            print('parse error: %s' % e)

    def parse_by_xpath(self, resp, rule):
        pass


getter = Getter()
