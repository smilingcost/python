#coding=utf-8
import os
import json
import re
import requests
import demjson
from lxml import etree
import lxml.html
import time

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
header = { "User-Agent" :USER_AGENT  }             #定义开头
count=0
for i in range(1,8):
      postData = { 'szWhich':'star',    #类型
              'nPage':i,        #页数
            'szSearch':
                     #  ''
                       'e000e77'
                         ,     #主播id ，空为查找所有主播
              'szSType':'A'
                      }
      url = 'http://afevent2.afreecatv.com:8120/app/rank/api.php'
      html_session = requests.Session()
      g=html_session.post(url,data = postData,headers = header).text
      loads = demjson.decode(g)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
      html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
      docs = lxml.html.fromstring(html).text
      names=re.findall(r'"bj_nick": "(.*?)",',docs)[0].encode('utf-8')
      with open('bj.csv','a')as f:         #保存最后爬取的信息
             s=str(names)
             f.write(s)

print names