#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import demjson
import json
#import simplejson as json
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
header = { "User-Agent" :USER_AGENT,
           "Referer": "http://afevent2.afreecatv.com:8120/app/rank/index.php"
           }
postData = { 'szWhich':'rookie',
'nPage':'1',
'szSearch':'',
'szSType':'A'
             }
url = 'http://afevent2.afreecatv.com:8120/app/rank/api.php'
html_session = requests.Session()
g=html_session.post(url,
                  data = postData,
                  headers = header).text

loads = demjson.decode(g)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串

print html

