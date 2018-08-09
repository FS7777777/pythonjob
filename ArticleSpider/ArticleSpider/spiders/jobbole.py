# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobble.com"]
    start_urls = ['http://blog.jobble.com/']

    def parse(self, response):
        pass
