# Pokud byste chtěla použít tento projekt bez Flask, stačí odkomentovat tyto pipelines,
# u pavouků místo 'from stack.stack.items import TagItem/StackItem' napsat 'from stack.items import TagItem/StackItem'
# a u pavouků odkomentovat nastavení pro pipelines v 'custom settings'
# následně do terminálu zadejte cd stack 
# a zadejte příkaz 'scrapy crawl stack' nebo 'scrapy crawl tag' (stack/tag záleží na tom co chcete scrapovat)
# Vše by mělo fungovat

'''from pymongo import MongoClient


class StackPipeline(object):
    collection_name = 'stack'

    def __init__(self):
        self.conn = MongoClient(
            'localhost', 27017  # pokud máte nějaký mongo server, nebo cokoliv, zde můžete změnit připoje
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
            'localhost', 27017  # pokud máte nějaký mongo server, nebo cokoliv, zde můžete změnit připojení
        )
        db = self.conn['Questions']
        self.collection = db['tags']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item'''
