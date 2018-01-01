#coding=utf-8
import requests
import sys
import time



#登录时需要POST的数据
data = {'areaCode':'0086',
'phoneNum':'18620521079',
'password':'d5d3ad33089c7741f0f30c7cd3cb091c',
'geetest_challenge':'81364de8c6857e40ca2e176dc86ca5a5',
'geetest_validate':'71e3e4dbb24c93717e59bfaa607555b5',
'geetest_seccode':'71e3e4dbb24c93717e59bfaa607555b5|jordan',
'redirect_url':'https://passport.douyu.com/member/login?ditchName=uc123&state=https%3A%2F%2Fwww.douyu.com%2Froom%2Ffollow',
't':'1514377152882',
'client_id':'1',
'sm_did':'WHJMrwNw1k/HVApevGCfyE4i9s5SLaiDc+fLjlVVPtJmtoHuHKPhP3DKZfNCSX9LiMYT1J+M50NHIcLvvZd+ucPh9b9nm2EQEvZwXnA6wGGfPCTWs5hojAA/GllaqVP3BfW5hgf5B6MYah7LzE4Pr2YJBFCxjl5RGFdyYlBQlGDZo4lsokyTgnIvsGrYyAiMRToxhSqtBzqwfbLhA26Z45mnHjwrFFo1lNKc8Xi0dha/zqTvTNUQt4gWD9gyODQ3xKQmj7bvpklgYc3EBVaOLMg==1487582755342',
'did':'',
'lang':'cn' }

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'https://passport.douyu.com/iframe/loginNew'

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)


#登录后才能访问的网页
url ='https://www.douyu.com/room/follow'

#发送访问请求
resp = session.get(url)

print resp.content