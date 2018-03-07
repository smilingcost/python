#coding=utf-8
#此模块与mssql数据库交互时，由于编码问题无法写入中文到数据库中！！！！！！
import pyodbc
import time
#数据库服务器信息
conn  = pyodbc.connect(DRIVER="{SQL Server Native Client 10.0}",SERVER="192.168.1.114",DATABASE="tae",UID="sa",PWD="*****", charset='UTF-8')  #用此语句连接，获得连接对象。

cursor = conn.cursor()  # %获得游标。

row=cursor.execute("""select  *
                      from [dbo].[info]

                      """)      #使用三引号的字符串来多行分解
#如果update/delete/insert记得要conn.commit()
 #否则数据库事务无法提交
print row.fetchall()
time.sleep(1)
pric='1u'
"""
#try:    #插入数据
cursor.execute(" insert into sj(titles) values ('pyodbc')")
print "已成功插入数据>>>"
#except:
 #   print "插入数据失败!!!"
time.sleep(1)
try:    #插入数据
    cursor.execute("delete from s where titles like '%pyodbc%'")
    print "已成功删除数据>>>"
except:
    print "删除数据失败!!!"

"""



conn.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
conn.close()


#sys.setdefaultencoding
