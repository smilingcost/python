#coding=utf-8

import requests
import re

def getContent(url):
         #使用requests.get获取知乎首页的内容
    r = requests.get(url)
          #request.get().content是爬到的网页的全部内容
    return r.content

#获取_xsrf标签的值
def getXSRF(url):
             #获取知乎首页的内容
    content = getContent(url)
            #正则表达式的匹配模式
    pattern = re.compile('<td class=listcellrow nowrap >(.*?)</td>')
             #re.findall查找所有匹配的字符串
    match = re.findall(pattern, content)
    xsrf = match
       #返回_xsrf的值
    return xsrf

            #登录的主方法
def login(baseurl,email,password):
 #post需要的表单数据，类型为字典
    login_data = {
            '_xsrf': getXSRF(baseurl),
            'password': password,
            'remember_me': 'true',
            'email': email,
    }
#设置头信息
    headers_base = {
        'Accept': 'text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Host': '192.168.1.93:93',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': 'http://192.168.1.93:93/config/app.jre?object_id=24',
    }
 #使用seesion登录，这样的好处是可以在接下来的访问中可以保留登录信息
    session = requests.session()
#登录的URL
    baseurl += ":93/login.jre"
 #requests 的session登录，以post方式，参数分别为url、headers、data
    content = session.post(baseurl, headers = headers_base, data = login_data)
 #成功登录后输出为 {"r":0,
 #"msg": "\u767b\u9646\u6210\u529f"
#}
    print content.text
#再次使用session以get去访问知乎首页，一定要设置verify = False，否则会访问失败
    s = session.get("http://192.168.1.93:93/config/list.jre?object_id=24&queryfield=&page=1&list_orderby=&list_orderv=&_=1499160552202", verify = False)
    print s.text.encode('utf-8')
      #把爬下来的知乎首页写到文本中
    f = open('renyi.txt', 'w')
    f.write(s.text.encode('utf-8'))

url = "http://192.168.1.93:93/config/list.jre?object_id=24&queryfield=&page=1&list_orderby=&list_orderv=&_=1499160552202"
#进行登录，将星号替换成你的知乎登录邮箱和密码即可
login(url,"daiding","zjg123")