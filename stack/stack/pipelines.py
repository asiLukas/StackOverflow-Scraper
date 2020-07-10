# If you would like to use this project without Flask, just uncomment these pipelines,
# for spiders instead of 'from stack.stack.items import TagItem / StackItem' write 'from stack.items import TagItem / StackItem'
# and for spiders, uncomment the settings for pipelines in 'custom settings'
# redirect to the folder where you have the scrapy.cfg file
# and enter the command 'scrapy crawl stack' or 'scrapy crawl tag' (stack / tag depends on what you want to scrap)
# Everything should work

'''from pymongo import MongoClient


class StackPipeline(object):
    collection_name = 'stack'

    def __init__(self):
        self.conn = MongoClient(
            'localhost', 27017  # mongo server port
        )
        db = self.conn['Questions']
        self.collection = db['questions']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item


class TagPipeline(object):
    collection_name = 'tag'

    def __init__(self):
        self.conn = MongoClient(
            'localhost', 27017  # mongo server port
        )
        db = self.conn['Questions']
        self.collection = db['tags']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item'''
