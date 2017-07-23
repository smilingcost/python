#coding=utf-8

import pymssql
import time
#数据库服务器信息
conn  = pymssql.connect(server="192.168.1.106", user="sa", password="zjg123", database="tae",charset="ISO-8859-1")  #用此语句连接，获得连接对象。charset="ISO-8859-1"根据每台电脑实际设置

cursor = conn.cursor()  # %获得游标。

cursor.execute("""select  *
                      from [dbo].[sj]

                      """)      #使用三引号的字符串来多行分解
#如果update/delete/insert记得要conn.commit()
 #否则数据库事务无法提交
print cursor.fetchall()
time.sleep(1)
pric1="pyodbc/Asus/华硕FXfx53笔记本电脑游戏本学生i7独显飞行堡垒15.6英寸游戏本学生i7独显飞行堡垒15.6英寸"
pric2="7777777777747"
pric3="71528"
pric4='https://detail.tmall.com/item.htm?id=543035827310&ns=1&abbucket=0&on_comment=1'
pric5='https://g-search2.alicdn.com/img/bao/uploaded/i4/i3/TB1S0t.SXXXXXbzXpXXXXXXXXXX_!!0-item_pic.jpg'
print pric1
try:    #插入数据
 cursor.execute("insert into sj (titles, price,selas,url,pi_url) values (%r,%s,%r,%r,%r)"%(pric1,pric2,pric3,pric4,pric5))

 print "已成功插入数据>>>"
except:
   print "插入数据失败!!!"
time.sleep(1)
try:    #插入数据
    cursor.execute("delete from s where titles like '%pyodbc%'")
    print "已成功删除数据>>>"
except:
    print "删除数据失败!!!"




conn.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
conn.close()


