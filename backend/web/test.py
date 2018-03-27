import requests
import json
from bs4 import BeautifulSoup

headers={'Content-Type': 'application/json'}
data = {'userName':'yangfei','passwd':'123456'}
r = requests.post('http://192.168.1.38:8080/api/users/login',data=json.dumps(data),headers=headers)
print(r.json())
print(json.dumps(data))