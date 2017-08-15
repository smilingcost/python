#coding=utf-8

import os
import json
import re
import requests
import demjson
from lxml import etree
import lxml.html
import time
import MySQLdb
import urllib

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
header = { "User-Agent" :USER_AGENT  }

def goods_url():
    list=[]
    name=raw_input("请输入需要爬取得名称：")
    page=raw_input("请输入需要爬取得页数：")
    data=urllib.quote(name)       #将中文转为url编码格式
    for i in range(0,int(page)):
         x=44*i
         list.append(x)
    print list                      #翻页规则，每页为44的倍数

    i=0
    for lit in list:
         url = 'https://s.taobao.com/search?app=mainSrp&q='+str(data)+'&cd=false&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s='+str(lit)
         goods_main(i,url)
         i+=1

def goods_main(i,url):
    try:
         print '开始爬虫第%s页--------------------------\n'%(int(i+1)),url
         time.sleep(1)
         htmls = requests.get(url).text
         docs = lxml.html.fromstring(htmls)
    except:
         print '获取网页失败，重新获取》》》》'
         goods_main(i,url)

    titles = docs.xpath('//script[8]/text()')[0]          #爬取网页script的文本内容
       #  print titles
    title=re.findall(r'g_page_config = (.*?shopcardOff":false}})',titles)[0]   #处理提取json格式里的内容
    url_1(title)
    print '第%s页爬虫结束--------------------------\n'%(int(i+1))



def url_1(title):          #打开文件

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
        info=titles[i]+','+price[i]+','+selas[i]+','+'https:'+url[i]+','+'https:'+pi_url[i]+'\n'
        infos=[titles[i],price[i],selas[i],'https:'+url[i],'https:'+pi_url[i]]
        g_url='https:'+url[i]
        goods_info(info,infos)
      #  goods_infos(g_url)
       # goods_pl(g_url)

        i+=1
def goods_info(info,infos):
    print '商品简单信息：\n----------------------------'
    print info
    try:
       with open('info.csv','a')as f:         #保存最后爬取的信息
           s=str(info)
           f.write(s)
       print '成功保存商品简单信息\n'
       goods_info_sql(infos)
    except:
        print '保存商品简单信息失败\n'

def goods_info_sql(infos):
       print "开始写入数据库--------------------\n"
       time.sleep(1)
       titles_sql=infos[0]
       price_sql =infos[1]
       selas_sql=infos[2]
       url_sql=infos[3]
       pi_url_sql=infos[4]
 # 打开数据库连接
       db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="zjg123",db="tae",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
       cursor = db.cursor()
# 使用execute方法执行SQL语句
       try:
          cursor.execute("insert into sj (titles, price,selas,url,pi_url) values ('%s','%s','%s','%s','%s')"%(titles_sql,price_sql,selas_sql,url_sql,pi_url_sql))
          print "已成功插入数据>>>\n",titles_sql,price_sql,selas_sql,url_sql,pi_url_sql
       except:
         print "插入数据失败!!!"
         db.rollback()
       db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
       db.close()
       time.sleep(1)

def goods_infos(g_url):
    print '商品详细信息：\n----------------------------'


def goods_pl(g_url) :
        print '商品评论信息：\n----------------------------\n',g_url

        html = requests.get(g_url).text
        doc = lxml.html.fromstring(html)
        title = doc.xpath('//script[3]/text()')[0]
        itemId=re.findall(r'itemId:"(.*?)"',title)[0]
        sellerId=re.findall(r'sellerId:"(.*?)"',title)[0]
        print  itemId,sellerId
        for page in range(1,2):
            g_pl_url='https://rate.tmall.com/list_detail_rate.htm?itemId='+str(itemId)+'&sellerId='+str(sellerId)+'&currentPage='+str(page)
            htmls=requests.get(g_pl_url,  headers = header).text
            titles=re.findall(r'"rateDetail":(.*?tags":""})',htmls)[0]
            loads = demjson.decode(titles)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
            pl_html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
          #  print pl_html
            displayUser=re.findall(r'"displayUserNick": "(.*?)",',pl_html)[0]
            auctionSku=re.findall(r'"auctionSku": "(.*?)",',pl_html)[0]
            rateDate =re.findall(r'"rateDate": "(.*?)"',pl_html)[0]
            rateContent=re.findall(r'"rateContent": "(.*?)",',pl_html)[0]
            print displayUser,auctionSku,rateDate,rateContent
            print '成功获取评论信息：\n'





 #在if __name__ == "__main__"：之后的语句作为模块被调用的时候(即被其它.py import 文件名)，语句之后的代码不执行；直接使用的时候，语句之后的代码执行。通常，此语句用于模块测试中使用。
if __name__ == '__main__':
   try:
     sj='titles'+','+'price'+','+'selas'+','+'url'+','+'pi_url'+'\n'
     print '获取数据的字段为',sj
     time.sleep(1)
     with open('info.csv','a')as f:
           s=str(sj)
           f.write(s)
     print "已写入列名>>>>"
   except:
       print "列名写入有误：请检查>>>>>\n"
   print '现在开始爬取内容：\n_______'
   time.sleep(1)
   goods_url()   #将page转化为整数，生成器要用for循环打印出，即是将函数赋予一个变量才可以进行遍历




