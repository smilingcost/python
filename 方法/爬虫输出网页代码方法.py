#coding=utf-8
#有些网页中文编码不是utf-8(/u5424)的输出后为乱码，用beautifulsoup处理后可以正常显示
#decode解码，encode编码
#resp.text返回的是Unicode型的数据。
#resp.content返回的是bytes型也就是二进制的数据str。
#取文本，可以通过r.text。
#则可以通过r.content。
#.json()返回的是json格式数据）



#coding=utf-8
import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
html = getHtml("http://192.168.1.93:93/universal/")
print html   #输出网页源代码   方法1

import urllib2
response = urllib2.urlopen('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9011')
html = response.read()
print html             #方法2

import urllib2
req = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page        #方法3

import re
import requests
url = 'http://dynamic.12306.cn/otn/board/query'
r = requests.get(url, verify=False)
x=r.text           #.text返回的是Unicode型的数据
print x                 #方法4

from bs4 import BeautifulSoup
import requests
response = requests.get("http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#find-all","html.parser")
soup = BeautifulSoup(response.content,"html.parser")
print soup


import requests
import lxml.html
from lxml import etree
url = 'http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml'
html = requests.get(url).text                 #编码问题换成.content。
doc = lxml.html.fromstring(html)  #或page = etree.HTML(html)
titles = doc.xpath('//div[@class="newsList"]/ul/li/a/text()')
href = doc.xpath('//div[@class="newsList"]/ul/li/a/@href')
i = 0
a=[]
for content in titles:
    results =str(i)+  titles[i]+'url:'+href[i]+'\n'   #每次读写后进行换行
    b=str(results)                        #若编码出现问题：x=results.replace(u'\xa0', u' ')
    with open('lxml_1.csv','a') as f:
     f.write(b)
    a.append(results)           #提取为list时，编码中文有问题，故采用分步提取（即提取一个url就先写入）
    i += 1
f.close()
print a