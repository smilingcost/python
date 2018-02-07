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

    captcha_url = 'http://www.gzmpc.com/gzmpcscm3/PicCheckCode?0.2864575034688368'
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
        'validateword':captcha
    }      #要按顺序排序
    login_url = 'http://www.gzmpc.com/gzmpcscm3/loginactionservlet'
    response = session.post(login_url, data=data, headers=headers)
   # print 'response.json() =', response.json()['msg']
    # 保存cookies到本地
    session.cookies.save()
    exp(email)
    time.sleep(1)
    exp_kc(email)
    time.sleep(1)

def exp(email):
    times =  int(round(time.time() * 1000))  #获取13位时间戳
    print times
    date={'_dc':str(times),
'startIndex':'0',
'pageRowNum':'1000',
'needpagecount':'true',
'gridcode':'func-salesflowsquery-grid',
'queryType':'query',
'dataSource':'salesflowsqueryquery',
'stagetype':'SALESFLOWS',
'stageid':'4',
'querymoduleid':'FuncSalesflowsqueryNorQuery',
'sumfieldnames':'goodsqty',
'fieldName_0':'credate__2',
'opera_0':'oper_equal',
'value1_0':'2018-02-05 23:59:59',    #时间
'fieldName_1':'credate',
'opera_1':'oper_between',
'value1_1':'2018-01-01 00:00:00',    #时间
'value2_1':'2018-02-05 23:59:59',    #时间
'oper_length':'2',
'page':'1',
'start':'0',
'limit':'25'
          }

    url = 'http://www.gzmpc.com/gzmpcscm3/extjsgridQueryServlet/query?_dc='+str(times)+'&startIndex=0&pageRowNum=1000&needpagecount=&gridcode=func-salesflowsquery-grid&queryType=query&dataSource=salesflowsqueryquery&stagetype=SALESFLOWS&stageid=4&querymoduleid=FuncSalesflowsqueryNorQuery&sumfieldnames=goodsqty&fieldName_0=credate__2&opera_0=oper_equal&value1_0=2018-02-05%2023%3A59%3A59&fieldName_1=credate&opera_1=oper_between&value1_1=2018-01-01%2000%3A00%3A00&value2_1=2018-02-05%2023%3A59%3A59&oper_length=2&page=1&start=0&limit=25'
    g=session.post(url,data = date,headers = headers)
    loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
    pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    pl = json.loads(pl_htmls)       #将json转化为字典
  #  print '页面响应码：', g.status_code,pl_htmls
    seles_dx(pl,email)

def seles_dx(pl,email):
    print  '获取销售数据！！'
    i=1
    name=email
    nemes=u'国盈'+name+u'销售流向.csv'
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
        rows=customname+','+goodsname+','+goodstype+','+salesdate+','+ goodsqty+','+ goodsunit+','+ lotno+','+unitprice+','+u'国盈'+'\n'
        try:
           with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存%s条数据------------%s--------------\n'%(i,name)
           i+=1
        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e

def exp_kc(email):
    times =  int(round(time.time() * 1000))  #获取13位时间戳
    print times
    date={'_dc':str(times),
'startIndex':'0',
'pageRowNum':'1000',
'needpagecount':'true',
'gridcode':'func-salesstquery-grid',
'queryType':'query',
'dataSource':'salesstqueryquery',
'stagetype':'SALESFLOWS',
'stageid':'4',
'querymoduleid':'FuncSalesstqueryNorQuery',
'sumfieldnames':'goodsqty',
'oper_length':'0',
'page':'1',
'start':'0',
'limit':'25'
          }

    url = 'http://www.gzmpc.com/gzmpcscm3/extjsgridQueryServlet/query?_dc='+str(times)+'&startIndex=0&pageRowNum=1000&needpagecount=true&gridcode=func-salesstquery-grid&queryType=query&dataSource=salesstqueryquery&stagetype=SALESFLOWS&stageid=4&querymoduleid=FuncSalesstqueryNorQuery&sumfieldnames=goodsqty&oper_length=0&page=1&start=0&limit=25'
    g=session.post(url,data = date,headers = headers)
    loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
    pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    pl = json.loads(pl_htmls)       #将json转化为字典
  #  print '页面响应码：', g.status_code,pl_htmls
    seles_dx_kc(pl,email)

def seles_dx_kc(pl,email):
    print  '获取库存数据！！'
    i=1
    name=email
    nemes=u'国盈'+name+u'库存.csv'
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
       # print  customname,goodsname, goodstype,salesdate, goodsqty, goodsunit, lotno,unitprice
       # print '--------------------------------------'
        rows=u'国盈'+','+goodsname+','+goodstype+','+ goodsqty+','+ goodsunit+','+ lotno+'\n'
        try:
           with open('./kc/'+nemes,'a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存%s条数据------------%s--------------\n'%(i,name)
           i+=1
        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e

def main1():
    email = '4364'
    password = '003658'
    captcha = get_captcha()
    login(email, password, captcha)

def main2():
    email = '837704'
    password = '181286'
    captcha = get_captcha()
    login(email, password, captcha)

def main3():
    email = '4188'
    password = '9043'
    captcha = get_captcha()
    login(email, password, captcha)

def main4():
    email = '843288'
    password = '000042'
    captcha = get_captcha()
    login(email, password, captcha)

def main5():
    email = '855295'
    password = '006335'
    captcha = get_captcha()
    login(email, password, captcha)

if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()   #后补的账号


