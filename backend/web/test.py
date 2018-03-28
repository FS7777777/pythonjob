import requests
import json
from bs4 import BeautifulSoup
from datafile import datalog
r = requests.get('https://movie.douban.com/top250')
print(r.content)
datalog.write(r.content)

