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
    return raw_input('请输入邮箱: ')


def get_password():
    return raw_input('请输入密码: ')


def login(email, password, captcha):
    data = {
        'password': password,
        'username': email,
        'verifycode': captcha
    }
    login_url = 'http://183.62.21.82:1666/wtyyecs/loginactionservlet'
    response = session.post(login_url, data=data, headers=headers)
   # print 'response.json() =', response.json()['msg']
    # 保存cookies到本地
    session.cookies.save()
    exp()


def exp():
    date={'startIndex':'0',
'pageRowNum':'50',
'gridcode':'func-flowquerymgr-grid',
'queryType':'query',
'dataSource':'ecs_salquery_v',
'querymoduleid':'FuncFlowquerymgrNorQuery',
'sumfieldnames':'goodsqty',
'sumfieldinfo':'',
'oper_length':'0'
          }

    url = 'http://183.62.21.82:1666/wtyyecs/extjsgridQueryServlet/query'
    g=session.post(url,data = date,headers = headers)
    loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
    pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    pl = json.loads(pl_htmls)       #将json转化为字典
    print '页面响应码：', g.status_code,pl_htmls
    seles_dx(pl)

def seles_dx(pl):
    print  '获取销售数据！！'
    for row in pl["rows"][0:-1]:
        customname=row["customname"]
        goodsname=row["goodsname"]
        goodstype=row["goodstype"]
        inputdate=row["inputdate"]
        goodsqty=row["goodsqty"]
        goodsunit=row["goodsunit"]
        lotno=row["lotno"]
        salprice=row["salprice"]
       # print  customname,goodsname, goodstype,inputdate, goodsqty, goodsunit, lotno,salprice
       # print '--------------------------------------'
        rows=customname+','+goodsname+','+goodstype+','+inputdate+','+ goodsqty+','+ goodsunit+','+ lotno+','+salprice+'\n'
        try:
           with open(u'大翔.csv','a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存数据--------------------------\n'

        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e
if __name__ == '__main__':

        email = get_email()
        password = get_password()
        captcha = get_captcha()
        login(email, password, captcha)

#http://183.62.21.82:1666/wtyyecs/loginSuccess.do
#244
#003658



