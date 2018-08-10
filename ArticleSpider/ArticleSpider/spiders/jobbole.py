# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from items import ArticleItem
import requests
from scrapy.utils.project import get_project_settings

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["yoursupin.com"]
    start_urls = ['https://www.yoursupin.com/page/2','https://www.yoursupin.com/page/3','https://www.yoursupin.com/page/4',
    'https://www.yoursupin.com/page/5','https://www.yoursupin.com/page/6','https://www.yoursupin.com/page/7']

    
    def __init__(self):
        self.browser = webdriver.Chrome()
        super(JobboleSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)
    
    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print ("spider closed")
        self.browser.quit()

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        post_nodes = response.css(".list_n1>a")
        
        for post_node in post_nodes:
            article_item = ArticleItem()
            article_item["url"] = post_node.css("::attr(href)").extract_first("")
            article_item["imge"] = post_node.css("img::attr(src)").extract_first("")
            article_item["content"] = post_node.css("img::attr(alt)").extract_first("")
            # 使用chromedriver时中间件无法下载图片，因为chromedriver会将图片url在浏览器打开，中间件部分又将页面返回给pipline
            # 导致下载图片问题，所以临时决定用requests处理图片下载
            images = requests.get(article_item["imge"])
            # 获取的文本实际上是图片的二进制文本
            img = images.content
            # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
            path = '%s\%s' % (get_project_settings().get('IMAGES_STORE'), article_item["imge"].split('/')[-1])
            print('------------------------------------------------')
            print(path)
            with open( path,'wb') as f:
                f.write(img)
            yield article_item



            # yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)
        
        #提取下一页并交给scrapy进行下载
        # next_url = response.css(".next.page-numbers::attr(href)").extract_first("")      
        # if next_url:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
