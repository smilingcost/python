#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import demjson
import json



url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv28183&productId=3701781&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
htmls = requests.get(url).text
title=re.findall(r'fetchJSON_comment98vv28183\((.*?"afterDays":0}]})',htmls)[0]
loads = demjson.decode(title)              #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型
html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串

print html