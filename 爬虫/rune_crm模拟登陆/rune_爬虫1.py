#coding=utf-8
import requests
import sys
import time



#登录时需要POST的数据
<<<<<<< HEAD
data = {'mbShortname':'*****',
         'mbPassword':'*****',
=======
data = {'mbShortname':'***',
         'mbPassword':'***',
>>>>>>> origin/master
        'valiNo':'3822',
        'Submit':'(unable to decode value)',
        'loginto':'runecrm' }

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'http://14.23.146.99:93/login/userlogin.jre'

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)


times =  int(round(time.time() * 1000))  #获取13位时间戳
print times

#登录后才能访问的网页
url ='http://14.23.146.99:93/config/list.jre?object_id=8&queryfield=&page=1&list_orderby=&list_orderv=&_='+str(times)

#发送访问请求
resp = session.get(url)

print resp.content.encode('utf-8')

#4 a6i1q4 j 4 i 6 n 3 g 5 u 4 i 6 @ 3 # 5 1 4 2 6 3 3

