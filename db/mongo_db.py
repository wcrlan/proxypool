import pymongo


class Mongodb(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['proxypool']
        self.collection = self.db['proxy']
        self.collection.create_index('address', unique=True)

    def insert(self, proxy):
        try:
            self.collection.insert_one(proxy)
            print('save %s to db' % proxy)
        except pymongo.errors.OperationFailure:
            pass

    def delete(self, condition):
        self.collection.delete_one(condition)

    def update(self, condition, value):
        self.collection.update(condition, {'$set': value})

    def get(self, count=1):
        items = self.collection.find({}, {'address': 1, '_id': 0}, limit=int(
            count)).sort('delay', pymongo.ASCENDING)
        result = [item['address'] for item in items]
        return result

    def all(self):
        items = self.collection.find({}, {'address': 1, '_id':0})
        for item in items:
            yield item['address']

    def count(self, condition=None):
        return self.collection.count({} if not condition else condition)


db = Mongodb()


if __name__ == '__main__':
    cli = db
    for i in range(2):
        cli.insert({"address": '101.132.186.{}:{}'.format(i+10, i+4341), 'delay': -1})

    print(cli.get(5))
    print(cli.count())
