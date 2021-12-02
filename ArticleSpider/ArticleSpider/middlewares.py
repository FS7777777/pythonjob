# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent


class ArticlespiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
        

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.support.select import Select, By
class JSPageMiddleware:

    #通过chrome请求动态网页
    def process_request(self, request, spider):
        if spider.name == "brighter_satellites":
            '''选择地理位置'''
            Select(spider.browser.find_element_by_xpath('//*[@id="ctl00_ddlLocation"]')).select_by_value("2151038")

            '''选择明亮卫星每日预报'''
            spider.browser.find_element_by_xpath('//*[@id="aspnetForm"]/table/tbody/tr[3]/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div/p[18]/a').click()

            '''选择最低亮度3.0'''
            spider.browser.find_element_by_xpath('//*[@id="ctl00_cph1_radioButtonsMag_0"]').click()

            '''选择傍晚'''
            spider.browser.find_element_by_xpath('//*[@id="ctl00_cph1_TimeSelectionControl1_radioAMPM"]/tbody/tr[2]/td/label').click()

            # print(tb_tbody.text)
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8", request=request)


class RandomUserAgentMiddlware:
    #随机更换user-agent
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        '''通过ua对象获取 random属性'''
        def get_ua():
            return getattr(self.ua, self.ua_type)
        
        print(get_ua())
        request.headers.setdefault('User-Agent', get_ua())

# class RandomProxyMiddleware(object):
#     #动态设置ip代理
#     def process_request(self, request, spider):
#         get_ip = get_random_proxy()
#         print(get_ip)
#         request.meta["proxy"] = get_ip