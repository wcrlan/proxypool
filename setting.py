# process, thread config
API_RUN = True
VALID_RUN = True
CRAWL_RUN = True

VALID_THREAD_NUM = 10
CRAWL_THREAD_NUM = 4

# API config
API_HOST = 'localhost'
API_PORT = 5000

# db config
DB_HOST = 'localhost'
DB_PORT = 27017
DATABASE = 'proxypool'
COLLECTION = 'proxy'


# valid_proxy config


VALID_URL = 'https://www.baidu.com/'

VALID_CYCLE = 5 * 60

# Crawl Proxy config
CRAWL_CYCLE = 30 * 60

PAGE_PER_SITE = 5

RULES = [
    {
        'urls': ['http://www.xicidaili.com/nn/%s' % i for i in range(1, PAGE_PER_SITE + 1)],
        'parse': 'css',
        'pattern': '#ip_list > tr:not(:first-child)',
        'target': {'ip': 'td:nth-child(2)', 'port': 'td:nth-child(3)'}
    },
    {
        'urls': ['https://www.kuaidaili.com/free/inha/%s/' % i for i in range(1, PAGE_PER_SITE + 1)],
        'parse': 'css',
        'delay': 1.,
        'pattern': '#list > table > tbody > tr',
        'target': {'ip': 'td:nth-child(1)', 'port': 'td:nth-child(2)'}
    },
    {
        'urls': ['http://www.66ip.cn/%s.html' % i for i in range(1, PAGE_PER_SITE)],
        'parse': 're',
        'pattern': r'<tr><td>((?:\d{,3}\.){3}\d{,3})</td><td>(.*?)</td><td>.*?</td><td>.*?</td><td>.*?</td></tr>',
        'target': {'ip': 0, 'port': 1}
    },
    {
        'urls': ['http://www.ip3366.net/?stype=1&page=%s' % i for i in range(1, PAGE_PER_SITE)],
        'parse': 'css',
        'pattern': '#list > table > tbody > tr',
        'target': {'ip': 'td:nth-child(1)', 'port': 'td:nth-child(2)'}
    }


]
