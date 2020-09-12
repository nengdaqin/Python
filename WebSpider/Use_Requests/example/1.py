import re
import requests
import pandas as pd


def get_page(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.text
	else:
	    return 'Crawl Failed'

def parse_html(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name.*?title="(.*?)".*?star.*?主演：'
    '(.*?)</p>.*?releasetime.*?上映时间：(.*?)</p>', re.S)
    result = re.findall(pattern, html)
    return result


url = 'https://maoyan.com/board/4?offset='
data = pd.DataFrame([], columns=['Name', 'Actors', 'Date', 'Region'])

for i in range(10):
	page_url = url + str(i * 10)
	html = get_page(page_url)
	result = parse_html(html)

	for item in result:
		rank = item[0]
		name = item[1]
		actors = item[2].strip()
		temp = item[3].split('(')
		if len(temp) == 1:
			date = temp[0]
			data.loc[rank, 'Date'] = date
		else:
			date = temp[0]
			region = temp[1][:-1]
			data.loc[rank, 'Date'] = date
			data.loc[rank, 'Region'] = region
		data.loc[rank, 'Name'] = name
		data.loc[rank, 'Actors'] = actors

data.to_csv('猫眼电影TOP100.csv', encoding='gbk')