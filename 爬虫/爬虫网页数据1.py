#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html

def url_1(n):                                #定义爬取得页数
       urls1=[]
       for i in range(1,n+1):
          url = 'http://www.kzj365.com/category-9-b0-min0-max0-page-'+str(i)+'-default-DESC-pre2.html'
          yield url_2(url)     #将url返回给url_2(url)，yield在python内部是当作list处理的

def url_2(url):                             #定义爬取的数据
     html = requests.get(url).content
     doc = lxml.html.fromstring(html)           #或page = etree.HTML(html)
     titles = doc.xpath('//div[@class="goodsInfo"]/a/span[1]/text()')
     price=doc.xpath('//div[@class="price"]/text()')
     href = doc.xpath('//div[@class="goodsInfo"]/a/@href')
     i=0
     a=[]
     for rr in titles:
        print url
        results = titles[i]+','+price[i]+','+'http://www.kzj365.com/'+href[i]+'\n'  #/n 进行换行
        print results
        b=str(results)
        with open('lxml_1.csv','a') as f:
         f.write(b)
        i += 1
     f.close()

if __name__ == '__main__':
    page=raw_input("请输入页数： ")
    for yy in url_1(int(page)):    #将page转化为整数
       print yy
7