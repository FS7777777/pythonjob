import sys
import os

from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'jobbole'])
# execute(['scrapy', 'crawl', 'gril'])
# execute(['scrapy', 'crawl', 'tle','-a','noardid=44884,49383,49384'])
# execute(['scrapy', 'crawl', 'weather'])
execute(['scrapy', 'crawl', 'brighter_satellites'])