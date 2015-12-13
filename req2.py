#-*- coding:utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
repeat = 'http://210.35.251.243/opac/item.php?marc_no=0000'
repeat2 = 'http://book.douban.com/subject/'

while True:
    book = raw_input('Enter the name of book which you need find:')
    def func():
        book1 = book
        if (book1 in ['百年孤独'.decode('utf-8').encode('gbk'), '苏菲的世界'.decode('utf-8').encode('gbk'),
                     '明朝那些事儿'.decode('utf-8').encode('gbk'), '平凡的世界'.decode('utf-8').encode('gbk'),
                     '300ЛОГИЧЕС...'.decode('utf-8').encode('gbk'), '狼图腾'.decode('utf-8').encode('gbk'),
                     '庐山导游'.decode('utf-8').encode('gbk'), '单片机应用技术'.decode('utf-8').encode('gbk'),
                     '新概念英语词汇练习'.decode('utf-8').encode('gbk')]):

            if (book1 == "百年孤独".decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '431036')

            elif (book1 == "苏菲的世界".decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '635654')

            elif (book1 == "明朝那些事儿".decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '620873')

            elif (book1 == "平凡的世界".decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '480777')

            elif (book1 == "300ЛОГИЧЕС...".decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '616356')

            elif (book1 == '狼图腾'.decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '368681')

            elif (book1 == '庐山导游'.decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '005460')

            elif (book1 == '单片机应用技术'.decode('utf-8').encode('gbk')):
                responses = requests.get(repeat + '649601')

            else:
                responses = requests.get(repeat + '333258')

            responses.encoding = 'utf-8'
            soup = BeautifulSoup(responses.text, 'lxml')
            item = soup.find(id="item_detail")
            return item.get_text()

        else:
            return 'Try again!!'
    fun = func()
    print fun

    if (book in ['百年孤独'.decode('utf-8').encode('gbk'), '苏菲的世界'.decode('utf-8').encode('gbk'),
                 '明朝那些事儿'.decode('utf-8').encode('gbk'),'新概念英语词汇练习'.decode('utf-8').encode('gbk'),
                 '狼图腾'.decode('utf-8').encode('gbk'),'单片机应用技术'.decode('utf-8').encode('gbk')]):
        def func2():
            book2 = book
            if (book2 == '百年孤独'.decode('utf-8').encode('gbk')):
                responses2 = requests.get(repeat2 + '1786670/', headers=head)

            elif (book2 == '苏菲的世界'.decode('utf-8').encode('gbk')):
                responses2 = requests.get(repeat2 + '3301179/', headers=head)

            elif (book2 == '明朝那些事儿'.decode('utf-8').encode('gbk')):
                responses2 = requests.get(repeat2 + '1873231/', headers=head)

            elif (book2 == '狼图腾'.decode('utf-8').encode('gbk')):
                responses2 = requests.get(repeat2 + '1022060/', headers=head)


            elif (book2 == '单片机应用技术'.decode('utf-8').encode('gbk')):
                responses2 = requests.get(repeat2 + '3209132/', headers=head)

            elif (book2 == '新概念英语词汇练习'.decode('utf-8').encode('gbk')):
                responses2 = requests.get(repeat2 + '1199897/', headers=head)
                
            responses2.encoding = 'utf-8'
            soup2 = BeautifulSoup(responses2.text, 'lxml')
            item2 = soup2.find(class_='intro')
            strings = str(item2).replace('<div class="intro">', '').replace('<p>', '').replace('</p>', '').replace('</div>', '')
            return strings.decode('utf-8').encode('gbk') 
        fun2 = func2()
        print fun2