import scrapy

from urllib import parse
import scrapy
from scrapy import signals
from scrapy.http import Request
from selenium import webdriver




class BrighterSatellitesSpider(scrapy.Spider):
    name = 'brighter_satellites'
    allowed_domains = ['heavens-above.com']
    start_urls = ['https://www.heavens-above.com']
    cookies_dict = dict()
    city_list = []

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie': 'bid=FyYqXADVlZw; _pk_id.100001.8cb4=87c25eac992a186a.1527238453.1.1527238453.1527238453.; _pk_ses.100001.8cb4=*; __utma=30149280.343087314.1527238454.1527238454.1527238454.1; __utmc=30149280; __utmz=30149280.1527238454.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.1.10.1527238454',
        'Host': 'www.heavens-above.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BrighterSatellitesSpider, cls).from_crawler(crawler, *args, **kwargs)
        ''' 从命令行参数中获取登录信息、city Id参数传递规则 citys=44884,12345 '''
        userName = kwargs.get('username')
        pwd = kwargs.get('pwd')
        citys = kwargs.get('citys')
        if  citys:
            cls.city_list = citys.split('')
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        #设置chromedriver不加载图片
        chrome_opt = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images":2}
        # chrome_opt.add_experimental_option("prefs", prefs)
        cls.browser = webdriver.Chrome(r"F:\tools\chromedriver_win32\chromedriver.exe",chrome_options=chrome_opt)
        cls.browser.get("https://www.heavens-above.com/login.aspx")
        '''登录'''
        cls.browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_UserName"]').send_keys(userName)
        cls.browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_Password"]').send_keys(pwd)
        cls.browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_LoginButton"]').click()

        cookies = cls.browser.get_cookies()
        for cookie in cookies:
            cls.cookies_dict[cookie['name']] = cookie['value']
        return spider


    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print ("spider closed")
        self.browser.quit()
    

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(url=u, cookies=self.cookies_dict, headers=self.headers, callback=self.parse)    

    def parse(self, response):
        
        yield from self.parse_detail(response)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(response.url)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        city = self.city_list.pop(0)
        if city:
            print(city)
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            yield Request(url=response.url, cookies=self.cookies_dict, meta = {'city':city}, callback=self.parse,dont_filter=True)
        else:
            yield Request(url=response.url, cookies=self.cookies_dict, meta = {'city':city}, callback=self.parse,dont_filter=False)
    def parse_detail(self, response):
        if not response.body:
            self.logger.warning(
                'can not find any response from current request {}'.format(response.request.url))
            return
        print(response.text) 
        '''开始筛选数据'''
        tb_tbody = response.xpath('//*[@id="aspnetForm"]/table/tbody/tr[3]/td[1]/table[3]/tbody/tr')

        print('================================================================================') 
        for tr in tb_tbody:
            sat = tr.xpath('td//text()').extract()
            yield {'city':response.meta.get('city'),'brighter_satellites': sat}