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


import json
import scrapy
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import redis

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

''' pipieline head => record all data to log file '''
class StoragePipleline(object):
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

''' pipieline  => download image by url '''
class DownloadImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if not item.get('image_url'):
            # raise DropItem('item not find any image_url:{}'.format(json.dumps(item)))
            return

        yield scrapy.Request(url=item.get('image_url'))

    def item_completed(self, results, item, info):
        ''' 如果item中没有url属性表示无需下载 '''
        if not item.get('image_url'):
            return item
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['imge_path'] = image_paths
        return item


''' pipieline tail => publish all data '''
class PublishPipleline(object):
    def __init__(self,redisPool):
        self.redisPool = redisPool
        self.r = redis.Redis(connection_pool=self.redisPool)
        self.p = self.r.pubsub(ignore_subscribe_messages=True)
    
    @classmethod
    def from_settings(cls,settings):
        """
        获取settings 文件redis配置
        """
        dbparams = dict(host=settings['REDIS_HOST'],port=settings['REDIS_PORT'],pd=settings['REDIS_PD'])
        redisPool = redis.ConnectionPool(host=dbparams['host'], port=dbparams['port'], db=0, password=dbparams['pd'])
        return cls(redisPool)

    def process_item(self, item, spider):
        ''' 数据存储到redis中 '''
        self.r.rpush('scarpy-1',json.dumps(item))
        # self.r.publish('msg',json.dumps(item))
        return item

    def close_spider(self, spider):
        ''' 发布数据采集完成通知 '''
        self.r.publish('msg','scrapy {0} finish'.format(spider.name))
        self.redisPool.disconnect()