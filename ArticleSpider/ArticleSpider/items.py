# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
#导入ES model
from models.es_types import ArticleType
#计算搜索建议用
from elasticsearch_dsl.connections import connections
es = connections.create_connection(ArticleType._doc_type.using)



class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def proc_input(value):
    return "[终结者]:"+value

def gen_suggests(index, info_tuple):
    '''根据字符串生成搜索建议数组，使用es的分词接口生成'''
    used_words = set()
    suggests = []
    for text, weight in info_tuple:
        if text:
            #调用es的analyze接口分析字符串
            words = es.indices.analyze(index=index, analyzer="ik_max_word", params={'filter':["lowercase"]}, body=text)
            anylyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"])>1])
            new_words = anylyzed_words - used_words
        else:
            new_words = set()

        if new_words:
            suggests.append({"input":list(new_words), "weight":weight})

    return suggests

def test_suggests(value):
    suggests = []
    if value.find('熟女')>0:
        suggests.append({"input":['苍老师'], "weight":10})
    if value.find('头条女神')>0:
        suggests.append({"input":['国产的啊'], "weight":5})
    if value.find('大学生')>0:
        suggests.append({"input":['没作业是吧'], "weight":5})
    if value.find('少女')>0:
        suggests.append({"input":['违规了啊'], "weight":0})

    return suggests

class ArticleItemLoader(ItemLoader):
    '''使用了ItemLoader scrapy.Field(output_processor=MapCompose())才起作用'''
    default_output_processor = TakeFirst()

class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    imge = scrapy.Field()
    content = scrapy.Field(output_processor=MapCompose(proc_input))
    imge_path = scrapy.Field()

    def save_to_es(self):
        article = ArticleType()
        article.url = self['url']
        article.imge = self["imge"]
        article.content = self["content"]
        # article.suggest = gen_suggests(ArticleType._doc_type.index, ((article.title,10),(article.tags, 7))
        article.suggest = test_suggests(self["content"])

        article.save()
