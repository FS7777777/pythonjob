import scrapy

from urllib import parse
import scrapy


class TLESpider(scrapy.Spider):
    name = 'tle'
    allowed_domains = ['celestrak.com']
    root_url = 'https://celestrak.com/satcat/tle.php?CATNR={}'
    start_urls = []

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie': 'bid=FyYqXADVlZw; _pk_id.100001.8cb4=87c25eac992a186a.1527238453.1.1527238453.1527238453.; _pk_ses.100001.8cb4=*; __utma=30149280.343087314.1527238454.1527238454.1527238454.1; __utmc=30149280; __utmz=30149280.1527238454.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.1.10.1527238454',
        'Host': 'www.celestrak.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TLESpider, cls).from_crawler(crawler, *args, **kwargs)
        ''' 从命令行参数中获取noradid 参数传递规则 noardid=44884,12345 '''
        noardid = kwargs.get('noardid')
        if  noardid:
            noardids = noardid.split(',')
            for id in noardids:
                cls.start_urls.append(cls.root_url.format(id))
        return spider

    def start_requests(self):
        print('==========================================================================')
        print(self.start_urls)
        for u in self.start_urls:
            yield scrapy.Request(url=u, headers=self.headers, callback=self.parse)

    def parse(self, response):
        if not response.body:
            self.logger.warning(
                'can not find any response from current request {}'.format(response.request.url))
            return

        tles = response.text
        print(tles)
        if not tles:
            self.logger.error('can not find any tle')
            return
        
        yield {"tles": tles}

