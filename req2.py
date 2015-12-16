#-*- coding:utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
repeat = 'http://210.35.251.243/opac/'
repeat2 = 'http://book.douban.com/subject/'

li = []
response1 = requests.get('http://210.35.251.243/opac/ajax_top_lend_shelf.php', headers = head)
response1.encoding = 'utf-8'
soup = BeautifulSoup(response1.text,'lxml')
links = soup.find_all('a')

for link in links:
    li.append(str(link.get('href')))

ll = soup.find_all('li')
i = 0
for eachbook in ll:
    i = i + 1
    print i,eachbook.get_text()

head2 = {'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Cache-Control':'max-age=0','Connection':'keep-alive','Cookie':'PHPSESSID=8333fbv85va32n2joig41onp44','Host':'210.35.251.243','Referer':'http://210.35.251.243/opac/item.php?marc_no=0000431036','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
num = input('Enter the number of each book which you want to search: ')
eachlink = repeat + li[(num-1)]
response2 = requests.get(eachlink, headers = head)
li2=[]

def func():
    response2.encoding = 'utf-8'
    eachitem = BeautifulSoup(response2.text, 'lxml')
    item = eachitem.find(id="item_detail")
    return item.get_text()


fun = func()
print fun