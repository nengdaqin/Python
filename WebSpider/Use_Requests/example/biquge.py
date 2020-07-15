import requests
import re
import lxml
from requests.exceptions import RequestException

url = 'http://www.xbiquge.la/55/55954/23397142.html'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/83.0.4103.116 Safari/537.36'
    }
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.text)
else:
    print("fail")



# pattern = re.compile('<div class=.*?<h3>(.*?)</h3>.*?class="ltitle">(.*?).*?<li>.*?'
#     'href="(.*?)">(.*?)</a></li>', re.S)
# items = re.findall(pattern, response.text)
# print(items)



