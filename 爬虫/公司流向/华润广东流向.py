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
from lxml import etree
import lxml.html

session = requests.session()
session.cookies =  cookielib.LWPCookieJar(filename='cookies')
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
}

def get_captcha():

    captcha_url = 'http://www.crgdpharm.com/code'
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
        'ckhid':email,
'ckhsn':password,
'mum':captcha,
'Submit':'(unable to decode value)'
    }#要按顺序排序
    login_url = 'http://www.crgdpharm.com/Login_check'
    response = session.post(login_url, data=data, headers=headers)
    session.cookies.save()
    exp(response,email)
    time.sleep(1)


def exp(response,email):
    #登录后才能访问的网页
    url ='http://www.crgdpharm.com/Service/Allfl?Mindate=2018-1-26&Maxdate=2018-2-5&Submit=+%B2%E9%BF%B4%CB%F9%D3%D0%B2%FA%C6%B7%B5%C4%C1%F7%CF%F2+'
    #发送访问请求
    response = session.get(url).content
    html=response
   # print html

    soup = BeautifulSoup(html, "html.parser")
    #docs=soup.find_all( 'tr')
    docs=[]
    docs1=soup.select('tr[bgcolor="#E6FFE6"]')   #CSS选择器,通过属性的值来查找
    for a in docs1:
       docs.append(a)
    docs2=soup.select('tr[bgcolor="#FFFFFF"]')
    for b in docs2:
       docs.append(b)
   # print docs
    i=1

    name=email
    nemes=u'华润广东'+name+u'销售流向.csv'
    t=u'医院名称'+','+u'商品名称'+','+u'规格'+','+u'日期'+','+ u'数量'+','+ u'单位'+','+ u'批号'+','+u'价格'+','+u'商业公司'+'\n'
    with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
        ss=str(t)
        f.write(ss)
    for d in docs:
      # print d
       seles_dx(d,email,nemes)
       print '成功爬取第%s条数据-------------------------'%(i)
       i+=1

def seles_dx(d,email,nemes):
    print  '获取销售数据！！'
    global count
    name=email
    docs=re.findall(r'<td.*?>(.*?)</td>',str(d))
    #print docs
    customname=docs[1].decode("utf-8")
    goodsname='华佗再造丸'.decode("utf-8")
    goodstype='8g*12袋/盒'.decode("utf-8")
    certdate=docs[0].decode("utf-8")
    goodsqty=docs[5].decode("utf-8")
    goodsunit=docs[6].decode("utf-8")
    lotno=docs[4].decode("utf-8")
    price=docs[7].decode("utf-8")
    gs='华润广东'.decode("utf-8")
  #  print  customname,goodsname, goodstype,certdate, goodsqty, goodsunit, lotno,price
    rows=customname+','+goodsname+','+goodstype+','+certdate+','+ goodsqty+','+ goodsunit+','+ lotno+','+price+','+gs+'\n'
    try:
        with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
            s=str(rows)
            f.write(s)
        print rows,'成功保存%s条数据------------%s--------------\n'%(count,name)
        count+=1
    except(Exception),e:
        print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e


def main1():
    email = '888482'
    password = '661890'
    captcha = get_captcha()
    login(email, password, captcha)





if __name__ == '__main__':
    count=1
    main1()





