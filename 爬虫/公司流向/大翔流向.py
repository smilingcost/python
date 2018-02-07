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

    captcha_url = 'http://183.62.25.218:6002/ecs/verifyimag.jsp'
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
    login_url = 'http://183.62.25.218:6002/ecs/loginactionservlet'
    response = session.post(login_url, data=data, headers=headers)
   # print 'response.json() =', response.json()['msg']
    # 保存cookies到本地
    session.cookies.save()
    exp(email)
    time.sleep(1)
    exp_kc(email)
    time.sleep(1)

def exp(email):
    date={'startIndex':'0',
'pageRowNum':'1000',
'gridcode':'func-flowquerymgr2-grid',
'queryType':'query',
'dataSource':'ecs_salquery_v',
'querymoduleid':'all',
'sumfieldnames':'goodsqty',
'sumfieldinfo':'',
'fieldName_0':'certdate',
'opera_0':'oper_big_equal',
'value1_0':'2018-01-01',       #时间
'fieldName_1':'certdatestart',
'opera_1':'oper_big_equal',
'value1_1':'2018-01-01',       #时间
'fieldName_2':'certdate',
'opera_2':'oper_small_equal',
'value1_2':'2018-02-02',       #时间
'fieldName_3':'certdateend',
'opera_3':'oper_small_equal',
'value1_3':'2018-02-02',      #时间
'oper_length':'4'
          }

    url = 'http://183.62.25.218:6002/ecs/extjsgridQueryServlet/query'
    g=session.post(url,data = date,headers = headers)
    loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
    pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    pl = json.loads(pl_htmls)       #将json转化为字典
 #   print '页面响应码：', g.status_code,pl_htmls
    seles_dx(pl,email)

def seles_dx(pl,email):
    print  '获取销售数据！！'
    i=1
    name=email
    nemes=u'广东大翔'+name+u'销售流向.csv'
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
        price=row["price"]
       # print  customname,goodsname, goodstype,certdate, goodsqty, goodsunit, lotno,price
       # print '--------------------------------------'
        rows=customname+','+goodsname+','+goodstype+','+certdate+','+ goodsqty+','+ goodsunit+','+ lotno+','+price+','+u'广东大翔'+'\n'
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
'pageRowNum':'1000',
'gridcode':'func-stockquerymgr2-grid',
'queryType':'query',
'dataSource':'ecs_stockdtlquery',
'querymoduleid':'all',
'sumfieldnames':'goodsqty',
'sumfieldinfo':'',
'fieldName_0':'certdate',
'opera_0':'oper_big_equal',
'value1_0':'2018-01-26',
'fieldName_1':'certdatestart',
'opera_1':'oper_big_equal',
'value1_1':'2018-01-26',
'fieldName_2':'certdate',
'opera_2':'oper_small_equal',
'value1_2':'2018-02-05',
'fieldName_3':'certdateend',
'opera_3':'oper_small_equal',
'value1_3':'2018-02-05',
'oper_length':'4'
          }

    url = 'http://183.62.25.218:6002/ecs/extjsgridQueryServlet/query'
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
    nemes=u'广东大翔'+name+u'库存.csv'
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
       # print  customname,goodsname, goodstype,certdate, goodsqty, goodsunit, lotno,price
       # print '--------------------------------------'
        rows=u'广东大翔'+','+goodsname+','+goodstype+','+ goodsqty+','+ goodsunit+','+ lotno+'\n'
        try:
           with open('./kc/'+nemes,'a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存%s条数据------------%s--------------\n'%(i,name)
           i+=1
        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e

def main1():
    email = 'gy0265'
    password = '003658'
    captcha = get_captcha()
    login(email, password, captcha)





if __name__ == '__main__':
    main1()





