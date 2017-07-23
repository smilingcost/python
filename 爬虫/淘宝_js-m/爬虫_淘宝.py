#coding=utf-8

import os
import json
import re
import requests
import demjson
from lxml import etree
import lxml.html
import time
import pyodbc
import pymssql

def url_1():
    list=[]
    page=raw_input("请输入需要爬取得页数：")
    for i in range(0,int(page)):
         x=44*i
         list.append(x)
    print list                      #翻页规则，每页为44的倍数

    i=0
    for lit in list:
         url = 'https://s.taobao.com/search?q=%E6%B8%B8%E6%88%8F%E6%9C%AC&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170701&sort=sale-desc&bcoffset=6&p4ppushleft=%2C44&s='+str(lit)
         print '开始爬虫第%s页'%(int(i+1)),url
         time.sleep(1)
         htmls = requests.get(url).text
         docs = lxml.html.fromstring(htmls)
         titles = docs.xpath('//script[7]/text()')[0]          #爬取网页script的文本内容
         title=re.findall(r'g_page_config = (.*?shopcardOff":false}})',titles)[0]   #处理提取json格式里的内容
         yield url_2(title)
         print '第%s页爬虫结束'%(int(i+1))
         i+=1
def url_2(title):          #打开文件

    loads = demjson.decode(title)              #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型
    html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串


    with open('tb.json','w')as f:         #保存需要获取的文本源文件
           r=str(html)
           f.write(r)

    titles=re.findall(r'"raw_title": "(.*?)"',html)        #定义需要爬取得内容
    price=re.findall(r'"view_price": "(.*?)"',html)
    selas=re.findall(u'"view_sales": "(.*?)人收货"',html)
    url   =re.findall(r'"comment_url": "(.*?)"',html)
    pi_url=re.findall(r'"pic_url": "(.*?)"',html)           #定义需要爬取得内容
    i=0
    for a in titles:
        time.sleep(0.6)
        sj=titles[i]+','+price[i]+','+selas[i]+','+'https:'+url[i]+','+'https:'+pi_url[i]+'\n'
        print sj

        with open('sj.csv','a')as f:         #保存最后爬取的信息
           s=str(sj)
           f.write(s)
        titles_sql=titles[i]
        price_sql=price[i]
        selas_sql=selas[i]
        url_sql='https:'+url[i]
        pi_url_sql='https:'+pi_url[i]
        print titles_sql,price_sql,selas_sql,url_sql,pi_url_sql
        mssql(titles_sql,price_sql,selas_sql,url_sql,pi_url_sql)
        i+=1

def mssql(titles_sql,price_sql,selas_sql,url_sql,pi_url_sql):        #将数据写入数据库
#数据库服务器信息
  conn  = pymssql.connect(server='192.168.31.132', user='sa', password='zjg123', database='tae',  charset='UTF-8')  #用此语句连接，获得连接对象。
  cursor = conn.cursor()  # %获得游标。
#如果update/delete/insert记得要conn.commit()
 #否则数据库事务无法提交
  try:    #插入数据
    cursor.execute("insert into sj (titles, price,selas,url,pi_url) values (%r,%r,%r,%r,%r)"%(titles_sql,price_sql,selas_sql,url_sql,pi_url_sql))       #变量名不能治values里面，需用%s
    print "已成功插入数据>>>\n>>>>"
  except:
    print "插入数据失败!!!\n>>>>"
  time.sleep(0.5)
  conn.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
  conn.close()




 #在if __name__ == "__main__"：之后的语句作为模块被调用的时候(即被其它.py import 文件名)，语句之后的代码不执行；直接使用的时候，语句之后的代码执行。通常，此语句用于模块测试中使用。
if __name__ == '__main__':
   try:
     sj='titles'+','+'price'+','+'selas'+','+'url'+','+'pi_url'+'\n'
     print '获取数据的字段为',sj
     time.sleep(1)
     with open('sj.csv','a')as f:
           s=str(sj)
           f.write(s)
     print "已写入列名>>>>"
   except:
       print "列名写入有误：请检查>>>>>\n"
   print '现在开始爬取内容：\n_______'
   time.sleep(1)
   try:
     for yy in url_1():    #将page转化为整数，生成器要用for循环打印出，即是将函数赋予一个变量才可以进行遍历
        time.sleep(1)
        print yy
   except:
     pass