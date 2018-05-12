#coding=utf-8

import pymssql
import time,datetime
import sys
import json
import MySQLdb

def main():
    x=open(u'逍客日志.json').read().encode('utf-8')
    pl_html = json.loads(x)       #将json转化为字典
    #print x
    x1=pl_html["value"]["items"]
    #print x1
    for a in x1:
     # print a
        name=a["sender"]["name"]
        unix_ts = a["createTime"]
        createTime = datetime.datetime.fromtimestamp(unix_ts)#将时间戳转换为具体日期
        text1=a["plan"]["reportContent"][0]["text"]
        text2=a["plan"]["planContent"][0]["text"]
        text={"a":text1.encode('utf-8')}
       # print name,createTime,text1,text2
        xk=name+','+str(createTime)+','+text1+','+text2+'\n'
        xks=[name,str(createTime),text1,text2]
        print xk
        try:
            with open('xk.csv','a')as f:         #保存最后爬取的信息
                 s=str(xk)
                 f.write(s)
                 print '成功保存日志信息---------\n'
        except(E),e:
            print '保存日志信息失败！！！！！！！！！！！！！！\n',e
        xk_sql(xks)

def xk_sql(infos):
       print "开始写入数据库--------------------\n"
       name=infos[0]
       createTime=infos[1]
       text1=infos[2]
       text2 =infos[3]
 # 打开数据库连接
       db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="zjg123",db="tae",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
       cursor = db.cursor()
# 使用execute方法执行SQL语句
       try:
          cursor.execute("insert into xk (name,createTime,text1,text2) values ('%s','%s','%s','%s')"%(name,createTime,text1,text2))
          print "已成功插入数据>>>----------------------\n",name,createTime,text1,text2
       except(Exception),e:
         print "插入数据失败!!!！！！！！！！！！！！！",e
         db.rollback()
       db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
       db.close()
       time.sleep(1)

if __name__ == '__main__':
    try:
     xk=u'业务员'+','+u'时间'+','+u'今日工作总结'+','+u'明日工作计划'+'\n'
     print '获取数据的字段为\n',xk
     time.sleep(1)
     with open('xk.csv','a')as f:
           s=str(xk)
           f.write(s)
           print "已写入列名>>>>1"
    except(Exception),e:
       print "列名写入有误：请检查>>>>>1\n",e
    time.sleep(1)
    star=time.time()
    main()
    last=time.time()-star
    print u'共耗时：%f 秒'%(last)