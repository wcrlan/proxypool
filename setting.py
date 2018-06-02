PORT = 5000

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

TEST_URL = 'https://www.baidu.com/'

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
