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
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
header = { "User-Agent" :USER_AGENT  }


def main():
    data=urllib.quote(s_name)       #将中文转为url编码格式
    i=0
    for page in range(1,int(s_page)+1):
         url = 'http://search.51job.com/list/030200,000000,0000,00,9,99,'+str(data)+',2,'+str(page)+'.html'
         job_main(i,url)
         i+=1

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def

def job_main(i,url):
    try:
         print '开始爬虫第%s页--------------------------\n'%(int(i+1)),url
         time.sleep(1)
         htmls = requests.get(url,headers=header).text
         docs = lxml.html.fromstring(htmls)
        # print docs
    except(Exception),e:
         print '获取网页失败，重新获取！！！！！！！！！！！！！',e
         job_main(i,url)
    job_main_url(docs)
    print '第%s页爬虫结束--------------------------\n'%(int(i+1))

#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def
def  job_main_url(docs):
    print '获取主页页面url信息'
    url_s = docs.xpath('//p[@class="t1 "]/span/a/@href')
    i=0
    for a in url_s:
       # time.sleep(0.6)
        url=url_s[i]
        job_info(url)
        i+=1
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def
def job_info(url):
    print '获取职位信息：\n----------------------------',url
    html = requests.get(url,headers=header).text
    doc = lxml.html.fromstring(html)
    soup = BeautifulSoup(html, "html.parser")
    time = re.findall(r'<span class="sp4"><em class="i4"></em>(.*?)</span>',html)[0].encode("ISO-8859-1").encode("utf-8")
    name = doc.xpath('//div[@class="cn"]/h1/text()')[0].encode("ISO-8859-1").encode("utf-8")
    ares = doc.xpath('//div[@class="cn"]/span/text()')[0].encode("ISO-8859-1").encode("utf-8")
    try:
       money = doc.xpath('//div[@class="cn"]/strong/text()')[0].encode("ISO-8859-1").encode("utf-8")
    except:
        money='null'
    company = doc.xpath('//div[@class="cn"]/p[@class="cname"]/a/text()')[0].encode("ISO-8859-1").encode("utf-8")
    people = re.findall(r'<span class="sp4"><em class="i3"></em>(.*?)</span>',html)[0].encode("ISO-8859-1").encode("utf-8")
    #--------
    try:
        fulis=soup.find_all(class_="t2")[0].encode("ISO-8859-1").encode("utf-8")
        fu=fulis.replace("<span>","").replace("</span>",";") .replace("</p>",";")       #替换一些不必要的字符串
        fuli=re.sub("<p class=(.*?)>", "", fu)                                    #正则替换一些不必要的字符串
    except:
        fuli='null'
    try:
        d1 = soup.find_all(class_="bmsg job_msg inbox")[0].encode("ISO-8859-1").encode("utf-8")          #正则替换一些不必要的字符串
        d2=re.sub("<div class=(.*?)>", "", d1)
        d3=re.sub("<span class=(.*?)>", "", d2).replace("<br/>","").replace("<br/>","").replace("</span>","").replace("</p>","").replace("</div>","")
        d4=re.sub("<a class=(.*?) href=(.*?)onclick=(.*?)</a>", "", d3)
        d5=re.sub("<p class=(.*?)>", "", d4)
        describes=re.sub("<a class=(.*?) href=(.*?)</a>", "", d5)

    except:
        describes = 'null'

    #网页为gb2312编码，需转化编码
    job= s_name+','+time+','+name+','+ares+','+money+','+company+','+people+','+fuli+','+describes+','+url+'\n'
    jobs=[s_name,time,name,ares,money,company,people,fuli,describes,url]

    try:
       with open('job_info.csv','a')as f:         #保存最后爬取的信息
           s=str(job)
           f.write(s)
       print '成功保存职位信息--------------------------\n'

    except(Exception),e:
        print '保存职位信息失败！！！！！！！！！！！！！！！！！！！！！\n',e
    job_info_sql(jobs)
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def
def job_info_sql(jobs):
       print "开始写入数据库-----------------------\n"
       s_name_sql=jobs[0]
       time_sql=jobs[1]
       name_sql=jobs[2]
       ares_sql=jobs[3]
       money_sql =jobs[4]
       company_sql=jobs[5]
       people_sql=jobs[6]
       fuli_url_sql=jobs[7]
       describes_sql=jobs[8]
       url_sql=jobs[9]
       print s_name_sql,time_sql,name_sql,ares_sql,money_sql,company_sql,people_sql,fuli_url_sql,describes_sql,url_sql
 # 打开数据库连接
       db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="zjg123",db="tbgoods",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
       cursor = db.cursor()
# 使用execute方法执行SQL语句
       try:
          cursor.execute("insert into tb_job_info (s_name,time,name,ares,money,company,people,fuli,describes,url) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(s_name_sql,time_sql,name_sql,ares_sql,money_sql,company_sql,people_sql,fuli_url_sql,describes_sql,url_sql))
          print "已成功插入数据>>>-------------------------\n"
       except(Exception),e:
         print "插入数据失败!!!！！！！！！！！！！！！",e
         db.rollback()
       db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
       db.close()
       time.sleep(1)
#------------------------def--------------------------------def-------------------------------def--------------------------------------def--------------------------def
if __name__ == '__main__':
    try:
     job='s_name'+','+'time'+','+'name'+','+'ares'+','+'money'+','+'company'+','+'people'+','+'fuli'+','+'describes'+','+'url'+'\n'
     print '获取数据的字段为\n',job
     time.sleep(1)
     with open('job_info.csv','a')as f:
           s=str(job)
           f.write(s)
           print "已写入列名>>>>1"
    except(Exception),e:
       print "列名写入有误：请检查>>>>>1\n",e

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