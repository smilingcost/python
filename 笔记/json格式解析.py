#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import demjson
import json
#import simplejson as json

urls = 'https://s.taobao.com/search?q=%E6%B8%B8%E6%88%8F%E6%9C%AC&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170701&sort=sale-desc'
htmls = requests.get(urls).text
docs = lxml.html.fromstring(htmls)           #或page = etree.HTML(html)
titles = docs.xpath('//script[7]/text()')[0]
title=re.findall(r'g_page_config = (.*?shopcardOff":false}})',titles)[0]

loads = demjson.decode(title)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串

print html
