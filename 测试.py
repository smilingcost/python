#coding=utf-8

import re
import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
}

s= requests.session()
data = {'username':'10000364',
        'password':'003658',
        'loginform':'yes'
        }   #from data信息
#post 换成登录的地址，
res=s.post('http://59.41.111.229:8091/bingo-gy-sso/v2?openid.ex.client_id=security&openid.mode=checkid_setup&openid.return_to=http%3A%2F%2F59.41.111.229%3A8091%2Flx%2Fopenid%3Freturn_url%3Dhttp%253A%252F%252F59.41.111.229%253A8091%252Flx%252Fportal%252Flayouts%252Fdefault%252Findex.jsp',data=data,headers=headers)  #网页登陆界面，Request Method:POST，Request URL:https://www.w3cschool.cn/checklogin
#换成抓取的地址
a=s.get('http://www.crgdpharm.com/Service/Index')    #需要获取数据的页面
print a.text
