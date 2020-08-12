from itemadapter import ItemAdapter
from pymongo import MongoClient
from .normalize import normalize_item

class WorkerPipeline:
    
    collection_name = 'cars'
    
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DATABASE') )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item_normalized = normalize_item( ItemAdapter(item).asdict() )
        self.db[self.collection_name].update_one( { "url_hash": item_normalized['url_hash'] }, {"$set": item_normalized }, upsert=True)
        return item