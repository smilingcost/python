# -*- coding:utf-8 -*-
# python-version: 3.51
import requests, time
from bs4 import BeautifulSoup
try:
    import cookielib
except:
    import http.cookiejar as cookielib
from PIL import Image
import json
import re
import demjson
import random

session = requests.session()
session.cookies =  cookielib.LWPCookieJar(filename='cookies')
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
}

def get_captcha():

    captcha_url = 'http://www.sysu-pharm.com/gdcenter/checkcode.asp'
    response = session.get(captcha_url, headers=headers)
    captcha_name = 'captcha.gif'
    with open(captcha_name, 'wb') as f:
        f.write(response.content)
    im = Image.open(captcha_name)
    im.show()
    return raw_input('请输入验证码: ')


def get_email():
    return raw_input('请输入账号: ')


def get_password():
    return raw_input('请输入密码: ')


def login(email, password, captcha):
    data = {
        'username':email,
        'password':password,
        'pwds':captcha,
        'submit':'单点登录'
    }      #要按顺序排序
    login_url = 'http://www.sysu-pharm.com/gdcenter/login.asp'
    response = session.post(login_url, data=data, headers=headers)
  #  print response.text
   # print 'response.json() =', response.json()['msg']
    # 保存cookies到本地
    session.cookies.save()

    exp(email,response)
    time.sleep(1)

def exp(email,response):
    url ='http://www.sysu-pharm.com/gdcenter/self_manage/self_manage_index.asp'
    #发送访问请求
    response = session.get(url).content
    html=response
    print html


    x=random.randint(0,88)
    y=random.randint(0,22)
    print x,y
    date={'keyA':'',
'keyB':'',
'keyC':'',
'key_STARTDATE':'2018-1-1',
'key_ENDDATE':'2018-1-29',
'imageField2.x':x,
'imageField2.y':y,
'page_rows':'10',
'org_id':'',
'org_name':''
          }

    url = 'http://www.sysu-pharm.com/gdcenter/client_order_price/index.asp'
    g=session.post(url,data = date,headers = headers)
  #  loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
  #  pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    pl = g.text      #将json转化为字典
    print '页面响应码：', g.status_code,pl
    seles_dx(pl,email)

def seles_dx(pl,email):
    print  '获取销售数据！！'
    i=1
    name=email
    nemes=u'中山医'+name+u'销售流向.csv'
    t=u'医院名称'+','+u'商品名称'+','+u'规格'+','+u'日期'+','+ u'数量'+','+ u'单位'+','+ u'批号'+','+u'价格'+','+u'商业公司'+'\n'
    with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
               ss=str(t)
               f.write(ss)
    for row in pl["rows"][0:-1]:   #[0:-1]除去最后合计项
        customname=row["customname"]
        goodsname=row["goodsname"]
        goodstype=row["goodstype"]
        salesdate=row["salesdate"]
        goodsqty=row["goodsqty"]
        goodsunit=row["goodsunit"]
        lotno=row["lotno"]
        unitprice=row["unitprice"]
       # print  customname,goodsname, goodstype,salesdate, goodsqty, goodsunit, lotno,unitprice
       # print '--------------------------------------'
        rows=customname+','+goodsname+','+goodstype+','+salesdate+','+ goodsqty+','+ goodsunit+','+ lotno+','+unitprice+','+u'中山医'+'\n'
        try:
           with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存%s条数据------------%s--------------\n'%(i,name)
           i+=1
        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e

def main1():
    email = '405011'
    password = '654321'
    captcha = get_captcha()
    login(email, password, captcha)

def main2():
    email = '837704'
    password = '181286'
    captcha = get_captcha()
    login(email, password, captcha)

if __name__ == '__main__':
    main1()
   # main2()

#未完成1111111111111111111111111111111111111111


