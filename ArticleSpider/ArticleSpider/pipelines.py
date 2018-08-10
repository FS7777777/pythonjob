# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# try:
#     from cStringIO import StringIO as BytesIO
# except ImportError:
#     from io import BytesIO

from PIL import Image
import io


import codecs
import json
import scrapy
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonExporterPipleline(object):
    #调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('articleexport.json', 'ab')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if not item.get('url'):
            raise DropItem('item not find any url:{}'.format(json.dumps(item)))

        yield scrapy.Request(url=item.get('url'))

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['imge_path'] = image_paths
        return item