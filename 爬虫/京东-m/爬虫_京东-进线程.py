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
    for i in range(1,int(s_page)+1):
         x=2*i-1
         list.append(x)
    print list                      #翻页规则，每页为奇数

    i=0
    for lit in list:
         url = 'https://search.jd.com/Search?keyword='+str(data)+'&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&page='+str(lit)
         jd_main(i,url)
         i+=1

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def jd_main(i,url):
    try:
         print '开始爬虫第%s页--------------------------\n'%(int(i+1)),url
         time.sleep(1)
         htmls = requests.get(url,headers=header).text
         docs = lxml.html.fromstring(htmls)
    except(Exception),e:
         print '获取网页失败，重新获取！！！！！！！！！！！！！',e
         jd_main(i,url)
    jd_main_url(docs)
    print '第%s页爬虫结束--------------------------\n'%(int(i+1))

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def jd_main_url(docs):
    print '获取商品页面url信息'
    itemId=docs.xpath('//div[@class="gl-i-wrap"]/div[@class="p-operate"]/a[1]/@data-sku')
    url_s = docs.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
    i=0
    for a in itemId:
       # time.sleep(0.6)
        if 'https' in url_s[i]:
           url=url_s[i]
        else:
           url='https:'+url_s[i]
        id=itemId[i]
        jd_info(url,id)
        jd_pl(id)
        i+=1

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def jd_info(url,id):
    print '商品信息：\n----------------------------',url,id
    price_url = 'https://p.3.cn/prices/mgets?skuIds=J_'+str(id)
    try:
       htmls = requests.get(price_url,headers=header).text
    except(Exception),e:
         print '获取商品网页失败，重新获取！！！！！！！！！！！！！',e
         jd_info(url,id)
    price=re.findall(r'"p":"(.*?)"}]',htmls)[0]
    #print price
    html = requests.get(url,headers=header).text
    doc = lxml.html.fromstring(html)
    try:
       store = doc.xpath('//div[@class="J-hove-wrap EDropdown fr"]/div/div/a/@title')[0]
    except:
        store='null'
    titles = doc.xpath('//div[@class="preview"]/div/img/@alt')[0]
    info=s_name.decode("utf-8")+','+id+','+store+','+titles+','+price+','+url+'\n'
    infos=[s_name.decode("utf-8"),id,store,titles,price,url]
    print info
    try:
       with open('jd_info.csv','a')as f:         #保存最后爬取的信息
           s=str(info)
           f.write(s)
       print '成功保存商品信息--------------------------\n'

    except(Exception),e:
        print '保存商品简单信息失败！！！！！！！！！！！！！！！！！！！！！\n',e
    jd_info_sql(infos)


#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def



def jd_info_sql(infos):
       print "开始写入数据库--------------------\n"
       s_name_sql=infos[0]
       id_sql=infos[1]
       store_sql=infos[2]
       title_sql =infos[3]
       price_sql=infos[4]
       url_sql=infos[5]
 # 打开数据库连接
       db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="zjg123",db="tae",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
       cursor = db.cursor()
# 使用execute方法执行SQL语句
       try:
          cursor.execute("insert into jd_info (s_name,id,store,titles,price,url) values ('%s','%s','%s','%s','%s','%s')"%(s_name_sql,id_sql,store_sql,title_sql,price_sql,url_sql))
          print "已成功插入数据>>>----------------------\n",s_name_sql,id_sql,store_sql,title_sql,price_sql,url_sql
       except(Exception),e:
         print "插入数据失败!!!！！！！！！！！！！！！",e
         db.rollback()
       db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
       db.close()
       time.sleep(1)
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def


def jd_pl(id) :
    print '商品评论信息：\n----------------------------\n',id
    for pl_page in range(1,2):
        pl_url='https://club.jd.com/comment/productPageComments.action?productId='+str(id)+'&score=0&sortType=5&page='+str(pl_page)+'&pageSize=10'
        print pl_url
        try:
           htmls=requests.get(pl_url,  headers = header).text
           loads = demjson.decode(htmls)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
           pl_htmls=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
           pl_html = json.loads(pl_htmls)       #将json转化为字典
          # print pl_htmls
           id=pl_html["productCommentSummary"]["productId"]
           selas=pl_html["productCommentSummary"]["commentCount"]
           for comments in pl_html["comments"]:  #pl_html["comments"]的键值为多个字典组成的list，遍历字典
                 user=comments["nickname"]
                 titles=comments["referenceName"]
                 sku=comments["productColor"]
                 date=comments["creationTime"]
                 content=comments["content"]
               #  print id,selas,user,titles,sku,date,content
                 pl_info=str(id)+','+str(selas)+','+user+','+titles+','+sku+','+date+','+content+'\n'
                 pl_infos=[id,selas,user,titles,sku,date,content]
                 try:
                     with open('jd_pl.csv','a')as f:         #保存最后爬取的信息
                       s=str(pl_info)
                       f.write(s)
                       print '成功保存商品评论信息---------\n'
                 except(E),e:
                    print '保存商品评论信息失败！！！！！！！！！！！！！！\n',e
                 jd_pl_sql(pl_infos)
        except(Exception),e:
                print "页面获取失败！！！！！！！！！！！！！！！",e
                pass

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def jd_pl_sql(pl_infos):
       print "开始写入评论数据到数据库--------------------\n"
       time.sleep(0.5)
       id_sql=pl_infos[0]
       selas_sql=pl_infos[1]
       user_sql =pl_infos[2]
       titles_sql=pl_infos[3]
       sku_sql=pl_infos[4]
       date_sql=pl_infos[5]
       content_sql=pl_infos[6]
 # 打开数据库连接
       db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="zjg123",db="tae",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
       cursor = db.cursor()
# 使用execute方法执行SQL语句
       try:
          cursor.execute("insert into jd_pl (id,selas,user,titles,sku,date,content) values ('%s','%s','%s','%s','%s','%s','%s')"%(id_sql,selas_sql,user_sql,titles_sql,sku_sql,date_sql,content_sql))
          print "已成功插入评论数据>>>---------------------\n",id_sql,selas_sql,user_sql,titles_sql,sku_sql,date_sql,content_sql
       except(Exception),e:
         print "插入评论数据失败！！！！！！！！！！！！！！！！！",e
         db.rollback()
       db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
       db.close()
     #  time.sleep(1)



#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

if __name__ == '__main__':
    try:
     jd='s_name'+','+'d'+','+'store'+','+'titles'+','+'price'+','+'url'+'\n'
     print '获取数据的字段为\n',jd
     time.sleep(1)
     with open('jd_info.csv','a')as f:
           s=str(jd)
           f.write(s)
           print "已写入列名>>>>1"
    except(Exception),e:
       print "列名写入有误：请检查>>>>>1\n",e
    try:
       pl='id'+','+'selas'+','+'user'+','+'titles'+','+'sku'+','+'date'+','+'content'+'\n'
       print '获取数据的字段为\n',pl
       with open('jd_pl.csv','a')as p:
           r=str(pl)
           p.write(r)
           print "已写入列名>>>>2"
    except(Exception),e:
       print "列名写入有误：请检查>>>>>2\n",e
    print '现在开始爬取内容：\n_______'
    time.sleep(1)
    s_name=raw_input("请输入需要爬取得名称：")
    s_page=raw_input("请输入需要爬取得页数：")
  #  s_name='电脑'
    #s_page='2'
    star=time.time()
    main()
    last=time.time()-star
    print u'共耗时：%f 秒'%(last)