import re
import redis


class RedisClient(object):

    def __init__(self, host='localhost', port=6379, password=None):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score):
        if not re.match(r'\d+\.\d+\.\d+\.\d+:\d+', proxy):
            return
        return self.db.zadd('proxypool', proxy, score)

    def pop(self, proxy):
        pass

    # def count(self):
        # return self.db.scard('proxypool:valid_proxy')
