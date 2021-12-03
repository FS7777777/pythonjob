import scrapy

from urllib import parse
import scrapy


class CloudChartSpider(scrapy.Spider):
    name = 'cloud_chart'
    allowed_domains = ['nmc.cn']
    start_urls = ['http://www.nmc.cn/publish/satellite/FY4A-true-color.htm']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie': 'bid=FyYqXADVlZw; _pk_id.100001.8cb4=87c25eac992a186a.1527238453.1.1527238453.1527238453.; _pk_ses.100001.8cb4=*; __utma=30149280.343087314.1527238454.1527238454.1527238454.1; __utmc=30149280; __utmz=30149280.1527238454.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.1.10.1527238454',
        'Host': 'www.nmc.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(url=u, headers=self.headers, callback=self.parse)

    def parse(self, response):
        if not response.body:
            self.logger.warning(
                'can not find any response from current request {}'.format(response.request.url))
            return

        chartContent = response.xpath('//*[@id="timeWrap"]/div')
        if not chartContent:
            self.logger.error('can not find any wather message')
            return

        for chart in chartContent:
            # transfer the webp to jpg
            image_url = chart.xpath('@data-img').get()
            data_time = chart.xpath('@data-time').get()
            yield {"image_url": image_url, "data_time": data_time}