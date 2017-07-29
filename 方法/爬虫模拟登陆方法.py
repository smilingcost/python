#coding=utf-8

import re
import requests
import json


s= requests.session()
data = {'username':'954950195@qq.com','password':'***'}   #from data信息
#post 换成登录的地址，
res=s.post('https://www.w3cschool.cn/checklogin',data)  #网页登陆界面，Request Method:POST，Request URL:https://www.w3cschool.cn/checklogin
#换成抓取的地址
a=s.get('https://www.w3cschool.cn/index/checkHeader')    #需要获取数据的页面
print a.text