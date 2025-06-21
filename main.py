from bs4 import BeautifulSoup
import requests

url = requests.get('https://techcrunch.com/feed/')
soup = BeautifulSoup(url.content, 'xml')
news = soup.find('item')
title =  news.title.text
link = news.link.text
publication_date = news.pubDate.text
description = news.description.text
print(description)