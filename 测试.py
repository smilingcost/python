#coding=utf-8
import re
import requests
from lxml import etree
import lxml.html
import demjson



urls = 'https://www.zhihu.com/people/json-20/activities'
htmls = requests.get(urls).text
docs = lxml.html.fromstring(htmls)           #或page = etree.HTML(html)
  #将 Python 对象编码成 JSON 字符串

print htmls