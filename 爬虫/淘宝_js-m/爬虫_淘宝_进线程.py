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
import multiprocessing
import threading

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
header = { "User-Agent" :USER_AGENT  }

def main():
    list=[]
    data=urllib.quote(s_name)       #将中文转为url编码格式
    for i in range(0,int(s_page)):
         x=44*i
         list.append(x)
    print list                      #翻页规则，每页为44的倍数

    i=0
    for lit in list:
         url = 'https://s.taobao.com/search?app=mainSrp&q='+str(data)+'&cd=false&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s='+str(lit)
         goods_main(i,url)
         i+=1
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def
def goods_main(i,url):
    try:
         print '开始爬虫第%s页--------------------------\n'%(int(i+1)),url
         time.sleep(1)
         htmls = requests.get(url,headers=header).text
         docs = lxml.html.fromstring(htmls)
    except(Exception),e:
         print '获取网页失败，重新获取！！！！！！！！！！！！！！！',e
         goods_main(i,url)
    titles = docs.xpath('//script[8]/text()')[0]          #爬取网页script的文本内容
       #  print titles
    title=re.findall(r'g_page_config = (.*?shopcardOff":false}})',titles)[0]   #处理提取json格式里的内容
    goods_main_url(title)
    print '第%s页爬虫结束--------------------------\n'%(int(i+1))

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def goods_main_url(title):          #打开文件
    print '页面信息----------------------'
    loads = demjson.decode(title)   #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型
    try:
        html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
    except(Exception),e:
         print '获取页面失败，重新获取！！！！！！！！！！！！！',e
    with open('tb.json','w')as f:         #保存需要获取的文本源文件
           r=str(html)
           f.write(r)
    itemId=re.findall(r'"nid": "(.*?)"',html)
    titles=re.findall(r'"raw_title": "(.*?)"',html)        #定义需要爬取得内容
    price=re.findall(r'"view_price": "(.*?)"',html)
    selas=re.findall(u'"view_sales": "(.*?)人收货"',html)
    url   =re.findall(r'"comment_url": "(.*?)"',html)
    pi_url=re.findall(r'"pic_url": "(.*?)"',html)           #定义需要爬取得内容
    i=0
    for a in titles:
        time.sleep(0.6)
        info=s_name.decode("utf-8")+','+itemId[i]+','+titles[i]+','+price[i]+','+selas[i]+','+'https:'+url[i]+','+'https:'+pi_url[i]+'\n'
        infos=[s_name.decode("utf-8"),itemId[i],titles[i],price[i],selas[i],'https:'+url[i],'https:'+pi_url[i]]
        g_url='https:'+url[i]
       # goods_info(info,infos)
      #  goods_infos(g_url)
      #  goods_pl(g_url)
        pool.apply_async(goods_info, (info,infos ))      #================_____多进程------------
      #  pool.apply_async(goods_pl, (g_url, ))      #================_____多进程------------
        i+=1
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def goods_info(info,infos):
    print '商品简单信息：\n----------------------------'
    print info
    goods_info_sql(infos)
    try:
       with open('tb_info.csv','a')as f:         #保存最后爬取的信息
           s=str(info)
           f.write(s)
       print '成功保存商品简单信息----------------------\n'

    except(Exception),e:
        print '保存商品简单信息失败！！！！！！！！！！！！！！！\n',e
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def goods_info_sql(infos):
       print "开始写入数据库--------------------\n"
       time.sleep(1)
       s_name_sql=infos[0]
       itemId_sql=infos[1]
       titles_sql=infos[2]
       price_sql =infos[3]
       selas_sql=infos[4]
       url_sql=infos[5]
       pi_url_sql=infos[6]
 # 打开数据库连接
       db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="zjg123",db="tbgoods",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
       cursor = db.cursor()
# 使用execute方法执行SQL语句
       try:
          cursor.execute("insert into tb_info (s_name,ids,titles, price,selas,url,pi_url) values ('%s','%s','%s','%s','%s','%s','%s')"%(s_name_sql,itemId_sql,titles_sql,price_sql,selas_sql,url_sql,pi_url_sql))
          print "已成功插入数据>>>---------------------------\n",titles_sql,price_sql,selas_sql,url_sql,pi_url_sql
       except(Exception),e:
         print "插入数据失败!!!！！！！！！！！！！！！",e
         db.rollback()
       db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
       db.close()
       time.sleep(1)
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def
def goods_infos(g_url):
    print '商品详细信息：\n----------------------------'

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def
def goods_pl(g_url) :
    print '商品评论信息：\n----------------------------\n',g_url
    html = requests.get(g_url,headers=header).text
    doc = lxml.html.fromstring(html)
    if 'detail.tmall' in g_url:
        print '此为天猫商品页面：'
        title = doc.xpath('//script[3]/text()')[0]
        itemId=re.findall(r'itemId:"(.*?)"',title)[0]
        sellerId=re.findall(r'sellerId:"(.*?)"',title)[0]
        print  itemId,sellerId
        for page in range(1,2):
            g_pl_url='https://rate.tmall.com/list_detail_rate.htm?itemId='+str(itemId)+'&sellerId='+str(sellerId)+'&currentPage='+str(page)
            print g_pl_url
            time.sleep(1)
            try:
              htmls=requests.get(g_pl_url,  headers = header).text
              titles=re.findall(r'"rateDetail":(.*?tags":""})',htmls)[0]
              loads = demjson.decode(titles)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
              pl_html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
          #  print pl_html
              user=re.findall(r'"displayUserNick": "(.*?)",',pl_html)
              sku=re.findall(r'"auctionSku": "(.*?)",',pl_html)
              date =re.findall(r'"rateDate": "(.*?)"',pl_html)
              content=re.findall(r'"rateContent": "(.*?)",',pl_html)
            #  print user,sku,date,content
              print '成功获取评论信息：\n--------------------------'
              i=0
              for a in user:
                 time.sleep(0.6)
                 pl_info=itemId+','+user[i]+','+sku[i]+','+date[i]+','+content[i]+'\n'
                 pl_infos=[itemId,user[i],sku[i],date[i],content[i]]
                 print itemId,user[i],sku[i],date[i],content[i]
                 goods_pl_sql(pl_infos)
                 i+=1
                 try:
                    with open('tb_pl.csv','a')as f:         #保存最后爬取的信息
                       s=str(pl_info)
                       f.write(s)
                       print '成功保存商品评论信息---------\n'
                 except(E),e:
                    print '保存商品评论信息失败！！！！！！！！！！！！！！！！\n',e
            except(Exception),e:
                print "页面获取失败",e
                pass
    elif 'item.taobao' in g_url:
        print '此为淘宝商品页面：'
        title = doc.xpath('//script[1]/text()')[0]
        itemId=re.findall(r"itemId           : '(.*?)',",title)[0]
        sellerId=re.findall(r"sellerId         : '(.*?)'",title)[0]
        print  itemId,sellerId
        for page in range(1,2):
            g_pl_url='https://rate.taobao.com/feedRateList.htm?auctionNumId='+str(itemId)+'&userNumId='+str(sellerId)+'&currentPageNum='+str(page)
            print g_pl_url
            time.sleep(1)
            try:
              htmls=requests.get(g_pl_url,  headers = header).text
              titles=re.findall(r'\((.*?qnaDisabled":true})',htmls)[0]
              loads = demjson.decode(titles)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
              pl_html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
          #  print pl_html
              user=re.findall(r'"nick": "(.*?)",',pl_html)
              sku=re.findall(r'"sku": "(.*?)",',pl_html)
              date =re.findall(r'"date": "(.*?)"',pl_html)
              content=re.findall(r'"content": "(.*?)",',pl_html)
             # print user,sku,date,content
              print '成功获取评论信息：-----------------------\n'
              i=0
              for a in user:
                 time.sleep(0.6)
                 pl_info=itemId+','+user[i]+','+sku[i]+','+date[i]+','+content[i]+'\n'
                 pl_infos=[itemId,user[i],sku[i],date[i],content[i]]
                 print itemId,user[i],sku[i],date[i],content[i]
                 goods_pl_sql(pl_infos)
                 i+=1
                 try:
                    with open('tb_pl.csv','a')as f:         #保存最后爬取的信息
                       s=str(pl_info)
                       f.write(s)
                       print '成功保存商品评论信息---------\n'
                 except(E),e:
                    print '保存商品评论信息失败！！！！！！！！！！！！！！\n',e
            except(Exception),e:
                print "页面获取失败！！！！！！！！！！！！！！！",e
                pass
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def goods_pl_sql(pl_infos):
       print "开始写入评论数据到数据库--------------------\n"
     #  time.sleep(1)
       itemid_sql=pl_infos[0]
       user_sql =pl_infos[1]
       sku_sql=pl_infos[2]
       date_sql=pl_infos[3]
       content_sql=pl_infos[4]
 # 打开数据库连接
       db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="zjg123",db="tae",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
       cursor = db.cursor()
# 使用execute方法执行SQL语句
       try:
          cursor.execute("insert into tb_pl (itemid,user,sku,date,content) values ('%s','%s','%s','%s','%s')"%(itemid_sql,user_sql,sku_sql,date_sql,content_sql))
          print "已成功插入评论数据>>>---------------------------\n",itemid_sql,user_sql,sku_sql,date_sql,content_sql
       except(Exception),e:
         print "插入评论数据失败!!!！！！！！！！！！！！！！！！",e
         db.rollback()
       db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
       db.close()
     #  time.sleep(1)


#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

 #在if __name__ == "__main__"：之后的语句作为模块被调用的时候(即被其它.py import 文件名)，语句之后的代码不执行；直接使用的时候，语句之后的代码执行。通常，此语句用于模块测试中使用。
if __name__ == '__main__':
   try:
     tb='s_name'+','+'itemId'+','+'titles'+','+'price'+','+'selas'+','+'url'+','+'pi_url'+'\n'
     print '获取数据的字段为\n',tb
     time.sleep(1)
     with open('tb_info.csv','a')as f:
           s=str(tb)
           f.write(s)
           print "已写入列名>>>>1"
   except(Exception),e:
       print "列名写入有误：请检查>>>>>1\n",e
   try:
       pl='itemid'+','+'user'+','+'sku'+','+'date'+','+'content'+'\n'
       print '获取数据的字段为\n',pl
       with open('tb_pl.csv','a')as p:
           r=str(pl)
           p.write(r)
           print "已写入列名>>>>2"
   except(Exception),e:
       print "列名写入有误：请检查>>>>>2\n",e

   print '现在开始爬取内容：\n_______'
   time.sleep(1)
   s_name=raw_input("请输入需要爬取得名称：")
   s_page=raw_input("请输入需要爬取得页数：")
   star=time.time()
   pool = multiprocessing.Pool(processes = 2)   #============_____多进程------------
   main()   #将page转化为整数，生成器要用for循环打印出，即是将函数赋予一个变量才可以进行遍历
   pool.close()      #=====================_____多进程------------
   pool.join()
   last=time.time()-star
   print u'共耗时：%f 秒'%(last)



