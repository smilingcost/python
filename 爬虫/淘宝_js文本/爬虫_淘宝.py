#coding=utf-8

import os
import json
import re
import requests
import demjson
from lxml import etree
import lxml.html
import time

def url_1():
    list=[]
    page=raw_input("请输入需要爬取得页数：")
    for i in range(0,int(page)):
         x=44*i
         list.append(x)
    print list                      #翻页规则，每页为44的倍数

    i=0
    for lit in list:
         url = 'https://s.taobao.com/search?q=%E6%B8%B8%E6%88%8F%E6%9C%AC&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170701&sort=sale-desc&bcoffset=6&p4ppushleft=%2C44&s='+str(lit)
         print url
         time.sleep(1)
         htmls = requests.get(url).text
         docs = lxml.html.fromstring(htmls)
         titles = docs.xpath('//script[7]/text()')[0]          #爬取网页script的文本内容
         title=re.findall(r'g_page_config = (.*?shopcardOff":false}})',titles)[0]   #处理提取json格式里的内容
         yield url_2(title)

def url_2(title):          #打开文件

    loads = demjson.decode(title)              #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型
    html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串


    with open('tb.json','w')as f:         #保存需要获取的文本源文件
           r=str(html)
           f.write(r)

    titles=re.findall(r'"raw_title": "(.*?)"',html)        #定义需要爬取得内容
    price=re.findall(r'"view_price": "(.*?)"',html)
    url   =re.findall(r'"comment_url": "(.*?)"',html)
    pi_url=re.findall(r'"pic_url": "(.*?)"',html)           #定义需要爬取得内容
    i=0
    for a in titles:
        time.sleep(0.6)
        sj=titles[i]+','+price[i]+','+'https:'+url[i]+','+pi_url[i]+'\n'
        print sj
        i+=1
        with open('sj.csv','a')as f:
           s=str(sj)
           f.write(s)

if __name__ == '__main__':
    for yy in url_1():    #将page转化为整数，生成器要用for循环打印出，即是将函数赋予一个变量才可以进行遍历
        time.sleep(1)
        print yy