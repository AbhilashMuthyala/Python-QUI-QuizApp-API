import requests
import urllib.request
import json
import html
from bs4 import BeautifulSoup

proxy_handler = urllib.request.ProxyHandler({'https': '<>',
                                             'http': '<>'})
opener = urllib.request.build_opener(proxy_handler)

response = opener.open("https://opentdb.com/api.php?amount=10&type=boolean")
data = response.read().decode('utf8')
json_data = json.loads(data)
question_data=json_data["results"]
