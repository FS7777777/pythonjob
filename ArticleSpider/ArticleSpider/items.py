# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def proc_input(value):
    return "[终结者]:"+value

class ArticleItemLoader(ItemLoader):
    '''使用了ItemLoader scrapy.Field(output_processor=MapCompose())才起作用'''
    default_output_processor = TakeFirst()

class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    imge = scrapy.Field()
    content = scrapy.Field(output_processor=MapCompose(proc_input))
    imge_path = scrapy.Field()
