import scrapy

from urllib import parse
import scrapy
from scrapy import signals
from selenium import webdriver




class BrighterSatellitesSpider(scrapy.Spider):
    name = 'brighter_satellites'
    allowed_domains = ['heavens-above.com']
    start_urls = ['https://www.heavens-above.com']
    cookies_dict = dict()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie': 'bid=FyYqXADVlZw; _pk_id.100001.8cb4=87c25eac992a186a.1527238453.1.1527238453.1527238453.; _pk_ses.100001.8cb4=*; __utma=30149280.343087314.1527238454.1527238454.1527238454.1; __utmc=30149280; __utmz=30149280.1527238454.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.1.10.1527238454',
        'Host': 'www.heavens-above.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BrighterSatellitesSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        #设置chromedriver不加载图片
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_opt.add_experimental_option("prefs", prefs)
        cls.browser = webdriver.Chrome(r"F:\tools\chromedriver_win32\chromedriver.exe",chrome_options=chrome_opt)
        cls.browser.get("https://www.heavens-above.com/login.aspx")
        # cls.browser.get("https://www.heavens-above.com/AllSats.aspx")
        '''登录'''
        cls.browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_UserName"]').send_keys('-')
        cls.browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_Password"]').send_keys('-')
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
            yield {"brighter_satellites": sat}

