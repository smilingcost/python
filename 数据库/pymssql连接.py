#coding=utf-8

import pymssql
import time
import sys

#数据库服务器信息
conn  = pymssql.connect(server="192.168.1.193", user="sa", password="*****", database="ren",charset="ISO-8859-1")  #用此语句连接，获得连接对象。charset="ISO-8859-1"根据每台电脑实际设置

cursor = conn.cursor()  # %获得游标。

cursor.execute("""select a.exp_date ,
sum(a.saleCount)
from oa_crm_whFlow a
left join rs_ygb s on s.YGBH=a.manager
left join OA_CRM_DZCPFWXX cp on cp.cpbh=a.cpbh
where isnull(a.org_id,1)=1 and isnull(a.enable,1)=1
      -- and s.ygxm='付欣'
group by a.exp_date,s.ygxm

                      """)      #使用三引号的字符串来多行分解,
#语句不能出现中文，不能用order by

#如果update/delete/insert记得要conn.commit()
 #否则数据库事务无法提交
info=cursor.fetchall()
print info
time.sleep(1)
"""
for row in info:
  try:
    titles=row[0] .encode("ISO-8859-1").encode("utf-8")   # 对中文字符串进行编码
    price=row[1].encode("ISO-8859-1")
    selas=row[2].encode("ISO-8859-1").encode("utf-8")
    url=row[3].encode("ISO-8859-1").encode("utf-8")
    pi_url=row[4] .encode("ISO-8859-1").encode("utf-8")
    print titles, price,selas,url,pi_url
  except(Exception),e:
      print e
conn.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
conn.close()

"""

"""
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

"""
#问题，读取nvarchar类型是，为乱码？？？，转码也不行