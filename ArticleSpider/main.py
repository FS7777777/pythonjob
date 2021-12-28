import sys
import os

from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'jobbole'])
# execute(['scrapy', 'crawl', 'gril'])
execute(['scrapy', 'crawl', 'tle','-a','noardid=44884,49383,49384'])
# execute(['scrapy', 'crawl', 'cloud_chart'])
# execute(['scrapy', 'crawl', 'brighter_satellites','-a','username=-','-a','pwd=-','-a','citys=2158841,2151038,1892811'])
# execute(['scrapy', 'crawl', 'weather','-a','positions=116.41,39.92','-a','key=-'])
