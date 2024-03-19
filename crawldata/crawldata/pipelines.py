# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import json
class MongoDBPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb+srv://giapchicuong:12345@cluster0.v32oryq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        self.db = self.client['tinhte']

    def process_item(self,item,spider):
        collection = self.db['dienthoai']
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error in pipeline: {e}")

class JsonDBPipeline:
    def process_item(self, item, spider):
        self.file = open('tinhte_dienthoai.json','a',encoding='utf-8')
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        self.file.close()
        return item
