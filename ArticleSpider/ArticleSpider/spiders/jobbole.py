# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from items import ArticleItem

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["yoursupin.com"]
    start_urls = ['https://www.yoursupin.com']

    
    def __init__(self):
        self.browser = webdriver.Chrome()
        super(JobboleSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)
    
    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print ("spider closed")
        self.browser.quit()

    def parse(self, response):
        post_nodes = response.css(".list_n1>a")
        
        for post_node in post_nodes:
            article_item = ArticleItem()
            article_item["url"] = post_node.css("::attr(href)").extract_first("")
            article_item["imge"] = post_node.css("img::attr(src)").extract_first("")
            article_item["content"] = post_node.css("img::attr(alt)").extract_first("")
            yield article_item



            # yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)
        
        #提取下一页并交给scrapy进行下载
        # next_url = response.css(".next.page-numbers::attr(href)").extract_first("")      
        # if next_url:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
