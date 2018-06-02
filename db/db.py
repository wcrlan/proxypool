import pymongo
from pymongo.errors import OperationFailure

from core.setting import DB_HOST, DB_PORT, DATABASE, COLLECTION


class Mongodb(object):
    def __init__(self, host, port, database, collection):
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[database]
        self.collection = self.db[collection]
        self.collection.create_index('address', unique=True)

    def insert(self, proxy):
        try:
            self.collection.insert_one(proxy)
            print('save %s to db' % proxy['address'])
        except OperationFailure:
            pass

    def delete(self, condition):
        self.collection.delete_one(condition)

    def update(self, condition, value):
        self.collection.update_one(condition, {'$set': value})

    def get(self, condiftion=None, count=1):
        items = self.collection.find({}, {'address': 1, '_id': 0}, limit=int(
            count)).sort('delay')
        result = [item['address'] for item in items]
        return result

    def get_valid(self):
        items = self.collection.find({'delay': {'$gte': 0}}, {
                                     'address': 1, '_id': 0}).sort('delay')
        result = [item['address'] for item in items]
        return result

    def all(self):
        items = self.collection.find({}, {'address': 1, '_id': 0})
        for item in items:
            yield item['address']

    def count(self, condition=None):
        return self.collection.count({} if not condition else condition)


db = Mongodb(host=DB_HOST, port=DB_PORT, database=DATABASE, collection=COLLECTION)


if __name__ == '__main__':
    cli = Mongodb()
    for i in range(2):
        cli.insert({"address": '101.132.186.{}:{}'.format(i + 10, i + 4341), 'delay': -1})

    print(cli.get(5))
    print(cli.count())
