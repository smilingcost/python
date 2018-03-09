#coding=utf-8
import re
import requests
from lxml import etree
import lxml.html
import demjson
import time
import json

def url_1(url):

  html = requests.get(url).text
  doc = lxml.html.fromstring(html)
  urls=doc.xpath('//div[@class="img-box"]/a/@href')[0]

  htmls = requests.get(urls).text
  docs = lxml.html.fromstring(htmls)
  titles = docs.xpath('//script[@type="text/javascript"]/text()')[3]
  title=re.findall(r'var msgList = (.*?status":2,"type":49}}]})',titles)[0]

  loads = demjson.decode(title)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
  htmlss=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
  return htmlss
url='http://weixin.sogou.com/weixin?type=1&s_from=input&query=excel%E4%B9%8B%E5%AE%B6&ie=utf8&_sug_=n&_sug_type_='
print url_1(url)

