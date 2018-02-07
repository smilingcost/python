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


session = requests.session()
session.cookies =  cookielib.LWPCookieJar(filename='cookies')
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
}

def get_captcha():

    captcha_url = 'http://183.62.21.82:1666/wtyyecs/verifyimag.jsp'
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
        'password': password,
        'username': email,
        'verifycode': captcha
    }#要按顺序排序
    login_url = 'http://183.62.21.82:1666/wtyyecs/loginactionservlet'
    response = session.post(login_url, data=data, headers=headers)
   # print 'response.json() =', response.json()['msg']
    # 保存cookies到本地
    session.cookies.save()
    exp(email)    #流向
    time.sleep(1)
    exp_kc(email)   #库存

def exp(email):
    date={'startIndex':'0',
'pageRowNum':'1000',
'gridcode':'func-flowquerymgr-grid',
'queryType':'query',
'dataSource':'ecs_salquery_v',
'querymoduleid':'FuncFlowquerymgrNorQuery',
'sumfieldnames':'goodsqty',
'sumfieldinfo':'',
'fieldName_0':'certdatestart',
'opera_0':'oper_big_equal',
'value1_0':'2018-01-26',     #时间
'fieldName_1':'certdate',
'opera_1':'oper_big_equal',
'value1_1':'2018-01-26',     #时间
'fieldName_2':'certdateend',
'opera_2':'oper_small_equal',
'value1_2':'2018-02-05',    #时间
'fieldName_3':'certdate',
'opera_3':'oper_small_equal',
'value1_3':'2018-02-05',     #时间
'oper_length':'4'
          }

    url = 'http://183.62.21.82:1666/wtyyecs/extjsgridQueryServlet/query'
    g=session.post(url,data = date,headers = headers)
    loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
    pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    pl = json.loads(pl_htmls)       #将json转化为字典
    print '页面响应码：', g.status_code,pl_htmls
    seles_dx(pl,email)

def seles_dx(pl,email):
    print  '获取销售数据！！'
    i=1
    name=email
    nemes=u'通用'+name+u'销售流向.csv'
    t=u'医院名称'+','+u'商品名称'+','+u'规格'+','+u'日期'+','+ u'数量'+','+ u'单位'+','+ u'批号'+','+u'价格'+','+u'商业公司'+'\n'
    with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
               ss=str(t)
               f.write(ss)
    for row in pl["rows"][0:-1]:   #[0:-1]除去最后合计项
        customname=row["customname"]
        goodsname=row["goodsname"]
        goodstype=row["goodstype"]
        certdate=row["certdate"]
        goodsqty=row["goodsqty"]
        goodsunit=row["goodsunit"]
        lotno=row["lotno"]
        salprice=row["salprice"]
       # print  customname,goodsname, goodstype,certdate, goodsqty, goodsunit, lotno,salprice
       # print '--------------------------------------'
        rows=customname+','+goodsname+','+goodstype+','+certdate+','+ goodsqty+','+ goodsunit+','+ lotno+','+salprice+','+u'通用'+'\n'
        try:
           with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存%s条数据------------%s--------------\n'%(i,name)
           i+=1
        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e

def exp_kc(email):
    date={'startIndex':'0',
'pageRowNum':'500',
'gridcode':'func-stockquerymgr-grid',
'queryType':'query',
'dataSource':'ecs_stockdtlquery',
'querymoduleid':'FuncStockquerymgrNorQuery',
'sumfieldnames':'goodsqty',
'sumfieldinfo':'',
'oper_length':'0'
          }

    url = 'http://183.62.21.82:1666/wtyyecs/extjsgridQueryServlet/query'
    g=session.post(url,data = date,headers = headers)
    loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
    pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    pl = json.loads(pl_htmls)       #将json转化为字典
   # print '页面响应码：', g.status_code,pl_htmls
    seles_dx_kc(pl,email)

def seles_dx_kc(pl,email):
    print  '获取库存数据！！'
    i=1
    name=email
    nemes=u'通用'+name+u'库存.csv'
    t=u'商业公司'+','+u'商品名称'+','+u'规格'+','+ u'数量'+','+ u'单位'+','+ u'批号'+'\n'
    with open('./kc/'+nemes,'a')as f:         #保存最后爬取的信息
               ss=str(t)
               f.write(ss)
    for row in pl["rows"][0:-1]:   #[0:-1]除去最后合计项
        goodsname=row["goodsname"]
        goodstype=row["goodstype"]
        goodsqty=row["goodsqty"]
        goodsunit=row["goodsunit"]
        lotno=row["lotno"]
       # print  customname,goodsname, goodstype,certdate, goodsqty, goodsunit, lotno,salprice
       # print '--------------------------------------'
        rows=u'通用'+','+goodsname+','+goodstype+','+ goodsqty+','+ goodsunit+','+ lotno+'\n'
        try:
           with open('./kc/'+nemes,'a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存%s条数据------------%s--------------\n'%(i,name)
           i+=1
        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e



def main1():
    email = '244'
    password = '003658'
    captcha = get_captcha()
    login(email, password, captcha)

def main2():
    email = '1596'
    password = '888888'
    captcha = get_captcha()
    login(email, password, captcha)

def main3():
    email = '1531'
    password = '888888'
    captcha = get_captcha()
    login(email, password, captcha)

if __name__ == '__main__':
    main1()
    main2()
    main3()
      #  email = get_email()
      #  password = get_password()
     #   captcha = get_captcha()
     #   login(email, password, captcha)

#http://183.62.21.82:1666/wtyyecs/loginSuccess.do
#244
#003658



