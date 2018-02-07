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


def login(email, password):
    data = {
        'LoginForm':'yes',
        'username':email,
        'password':password
    }      #要按顺序排序
    login_url = 'http://59.41.111.229:8091/lx/openid?return_url=http%3A%2F%2F59.41.111.229%3A8091%2Flx%2F&openid.ex.service_ticket=STcff13fa9f98f4b6bab65f28df407cf45&openid.mode=id_res'
    response = session.post(login_url, data=data, headers=headers)
   # print 'response.json() =', response.json()['msg']
    # 保存cookies到本地
    session.cookies.save()
    exp(email)


def exp(email):
    date={"orderBy":{"fieldName":"","orderMethod":""},"filterSet":{"user_id":"20000051","stopflag":"10","currentpage":"","pz":"","goods":"","begdate":"2018-01-01","enddate":"2018-01-29","producer":"","ownerid":"3","csttype":"医院直销,零售直销,其他医疗直销,区域分销,全国分销,待定,供应商,恒兴销售","area":""},"total":0}

    url = 'http://59.41.111.229:8091/bingo-gy-flow/grid/query?dataQuerier=&sumSqlId=&gridRecordConverter=null&gridColumnIds=newcreatedate,goods,goodsname,spec,producer,newcstcode,newcstname,sendaddr,qty,unit,forecastid,billname,area,csttype,CompanyName&sqlId=gylxsale.lx_sale_list&countSqlId=&daoName='
    g=session.post(url,data = date,headers = headers)
   # loads = demjson.decode(g.text)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
   # pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
   # pl = json.loads(pl_htmls)       #将json转化为字典
    pl=g.text
    print '页面响应码：', g.status_code,pl
    seles_dx(pl,email)

def seles_dx(pl,email):
    print  '获取销售数据！！'
    i=1
    name=email
    nemes=u'广东粤兴'+name+u'销售流向.csv'
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
        rows=customname+','+goodsname+','+goodstype+','+salesdate+','+ goodsqty+','+ goodsunit+','+ lotno+','+unitprice+','+u'广东粤兴'+'\n'
        try:
           with open('./lx/'+nemes,'a')as f:         #保存最后爬取的信息
               s=str(rows)
               f.write(s)
           print rows,'成功保存%s条数据------------%s--------------\n'%(i,name)
           i+=1
        except(Exception),e:
             print '保存数据失败！！！！！！！！！！！！！！！！！！！！！\n',e

def main1():
    email = '20000051'
    password = '003658'

    login(email, password)


if __name__ == '__main__':
    main1()


#未完成1111111111111111111111111111111111111111

