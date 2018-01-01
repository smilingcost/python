#coding=utf-8

import requests
import sys
import time
from bs4 import BeautifulSoup
from lxml import etree
import lxml.html

def main(s_page):   #处理登陆信息

    times =  int(round(time.time() * 1000))  #获取13位时间戳
    print times
    for page in range(1,int(s_page)+1):
     #登录后才能访问的网页
      url = 'http://192.168.1.193:93/config/list.jre?object_id=24&queryfield=&page='+str(s_page)+'&list_orderby=&list_orderv=&_='+str(times)

      #浏览器登录后得到的cookie，也就是刚才复制的字符串，浏览器不能关闭
      cookie_str = r'__guid=15518966.143138523183509650.1506303722116.3914; ASPSESSIONIDSQRATRAB=IKGBABNAGNDLCJCNFNJBFNNA; monitor_count=66; rune_mbShortname=''; rune_mbPassword=''; rune_cookietime=0'

      #把cookie字符串处理成字典，以便接下来使用
      cookies = {}
      for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

      #设置请求头
      headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

      #在发送get请求时带上请求头和cookies
      html = requests.get(url, headers = headers, cookies = cookies).content
      #  print html.encode('utf-8')
      run_lx(html)
      print '爬虫完成第%s页'%(page)

def run_lx(html):
    print '开始爬取流向信息：'
  # soup = BeautifulSoup(html, "html.parser")
  # docs=soup.find_all( class_="listcellrow")
    doce = lxml.html.fromstring(html)
    doces=doce.xpath('//td[@class="listcellrow"]/text()')
  #  print len(doces),doces
    num=len(doces)/8  #数据条数，每条数据8个字段
    print num
    global count,counts
    for i in range(1,num+1):
      num1=int(8*(i-1))
      num2=int(8*i)
      rows=doces[num1:num2]
      rowe=[]
      for row in rows:
        try:
          #print doc.encode("ISO-8859-1").encode("utf-8")
          r=row.encode("ISO-8859-1").encode("utf-8")
          rowe.append(r)
          counts+=1
        except(Exception),e:
            print e
            count+=1
            pass
      for rowes in rowe:
        print rowes
      print  '---------------------------------------------------------------------------'
      print '爬取信息%s！！！出错信息%s！！！'%(counts,count)
if __name__ == '__main__':
   print '现在开始爬取内容：\n_______'
   time.sleep(1)
   s_page=raw_input("请输入需要爬取得页数：")
   star=time.time()
   count=0
   counts=0
   main(s_page)
   last=time.time()-star
   print u'共耗时：%f 秒'%(last)
