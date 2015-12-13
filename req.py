#-*-coding:utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup


responses = requests.get('http://210.35.251.243/opac/ajax_top_lend_shelf.php')  # 得到一个响应对象
responses.encoding = 'utf-8'  # 将相应对象转码为UTF-8
# 使用beautifulsoup的lxml解析器解析获取的相应对象的代码
soup = BeautifulSoup(responses.text, 'lxml')
# 找到id="search_container_center"的代码
hotbook = soup.find(id="search_container_center")
print hotbook.get_text()  # 将找到的代码中的文本内容输出

repeat = 'http://210.35.251.243/opac/item.php?marc_no=0000'
links = ['431036', '635654', '620873', '480777','616356', '368681', '005460', '649601', '333258']

for link in links:
    reallink = repeat + link
    responses = requests.get(reallink)
    responses.encoding = 'utf-8'
    soup = BeautifulSoup(responses.text, 'lxml')
    eachbook = soup.find(id="item_detail")
    print eachbook.get_text()
