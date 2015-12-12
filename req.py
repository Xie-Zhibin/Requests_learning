#-*-coding:utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

responses = requests.get('http://210.35.251.243/opac/ajax_top_lend_shelf.php') #得到一个响应对象
responses.encoding='utf-8' #将相应对象转码为UTF-8
soup = BeautifulSoup(responses.text,'lxml') #使用beautifulsoup的lxml解析器解析获取的相应对象的代码
hotbook = soup.find(id="search_container_center") #找到id="search_container_center"的代码
print hotbook.get_text() #将找到的代码中的文本内容输出
