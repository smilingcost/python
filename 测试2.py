#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import demjson
import json
#import simplejson as json



htmls=requests.get('https://club.jd.com/comment/productPageComments.action?productId=4163951&score=0&sortType=5&page=1&pageSize=10').text

loads = demjson.decode(htmls)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
pl_html = json.loads(pl_htmls)       #将json转化为字典
print pl_htmls
id=pl_html["productCommentSummary"]["productId"]
selas=pl_html["productCommentSummary"]["commentCount"]
for comments in pl_html["comments"]:  #pl_html["comments"]的键值为多个字典组成的list，遍历字典
    user=comments["nickname"]
    titles=comments["referenceName"]
    sku=comments["productColor"]
    date=comments["creationTime"]
    content=comments["content"]
    print id,selas,user,titles,sku,date,content


