#coding=utf-8

import requests
import sys
import time
from bs4 import BeautifulSoup
from lxml import etree
import lxml.html

def main():   #处理登陆信息
      url='http://www.crgdpharm.com/Service/Allfl?Mindate=2018-1-1&Maxdate=2018-2-1&Submit=+%B2%E9%BF%B4%CB%F9%D3%D0%B2%FA%C6%B7%B5%C4%C1%F7%CF%F2+'

      #浏览器登录后得到的cookie，也就是刚才复制的字符串，浏览器不能关闭
      cookie_str = r'Cookie:__guid=115509120.1637993098062158800.1501490558922.2207; ASPSESSIONIDCARATQBQ=CCFOHPEBDDKGFJJPJDAFFHCN; monitor_count=14'

      #把cookie字符串处理成字典，以便接下来使用
      cookies = {}
      for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

      #设置请求头
      headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

      #在发送get请求时带上请求头和cookies
      html = requests.get(url, headers = headers, cookies = cookies).content
      print html.encode('utf-8')

      print '爬虫完成第%s页'%(page)


if __name__ == '__main__':
   print '现在开始爬取内容：\n_______'
   time.sleep(1)

   main()
   last=time.time()-star
   print u'共耗时：%f 秒'%(last)