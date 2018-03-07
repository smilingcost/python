# -*- coding: UTF-8 -*-

import MySQLdb
import time
import pymssql

def mysql(titles, price,selas,url,pi_url):
    print '开始写入mysql数据库>>>\n'
    # 打开数据库连接
    db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="*****",db="tae",charset="utf8") #将localhost改为127.0.0.1，不然出错
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT * from sj")
    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchall()
   # print  data

    try:    #插入数据
       cursor.execute("insert into sj (titles, price,selas,url,pi_url) values ('%s','%s','%s','%s','%s')"%(titles, price,selas,url,pi_url))

       print "已成功插入数据>>>"
    except(Exception),e:
       print "插入数据失败!!!",e
       time.sleep(1)
    db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
    db.close()
"""
try:    #插入数据
    cursor.execute("delete from s where titles ")
    print "已成功删除数据>>>"
except:
    print "删除数据失败!!!"
   # 发生错误时回滚
  #  db.rollback()
"""
# 关闭数据库连接
def mssql():
    #数据库服务器信息
    print "开始获取sql server 数据库信息>>>\n"
    conn  = pymssql.connect(server="192.168.1.114", user="sa", password="*****", database="tae",charset="ISO-8859-1")  #用此语句连接，获得连接对象。charset="ISO-8859-1"根据每台电脑实际设置

    cursor = conn.cursor()  # %获得游标。

    cursor.execute("""select  *
                      from [dbo].[info]

                      """)      #使用三引号的字符串来多行分解
    #如果update/delete/insert记得要conn.commit()
     #否则数据库事务无法提交
    info=cursor.fetchall()
    time.sleep(1)
    for row in info:
       titles=row[0] .encode("ISO-8859-1").encode("utf-8")             # 对中文字符串进行编码
       price=row[1].encode("utf-8")                      #写入mysql时，提示为gbk，需将字符串编码为.encode("utf-8")
       selas=row[2].encode("utf-8")               #写入mysql时，提示为gbk，需将字符串编码为.encode("utf-8")
       url=row[3].encode("utf-8")
       pi_url=row[4].encode("utf-8")
       print '成功获取数据>>\n',titles, price,selas,url,pi_url
       time.sleep(1)
       mysql(titles, price,selas,url,pi_url)
    conn.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
    conn.close()

if __name__ == '__main__':
    mssql()
