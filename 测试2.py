#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import demjson
import json


s= requests.session()
data = {'username':'954950195@qq.com','password':'***'}
#post 换成登录的地址，
res=s.post('https://www.w3cschool.cn/checklogin',data)
#换成抓取的地址
a=s.get('https://www.w3cschool.cn/my')
print a.text