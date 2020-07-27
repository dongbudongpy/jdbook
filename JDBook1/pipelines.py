# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
import redis
# 选择存入本地或者数据库


# json文件的管道
class Jdbook1Pipeline(object):
    def open_spider(self, spider):
        self.file = open('book.json','wb')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

# redis数据库的管道
class Jdbook1RedisPipeline(object):
    def open_spider(self, spider):
        self._redis = redis.StrictRedis()
        self._save_key = 'book_key'

    def process_item(self, item, spider):
        item_str = str(dict(item))
        self._redis.lpush(self._save_key, item_str)
        return item