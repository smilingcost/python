# -*- coding: UTF-8 -*-

import MySQLdb
import time
# 打开数据库连接
db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="*****",db="tbgoods",charset="utf8") #将localhost改为127.0.0.1，不然出错
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("""
               SELECT p.itemid,i.titles,count(*)
               from tb_pl p
               left join tb_info i on p.itemid=i.ids
               group by p.itemid,i.titles
               """)



# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchall()
#print  data
for row in data:
    titles=row[0]  # 对中文字符串进行编码
    price=row[1]
    selas=row[2]
  #  url=row[3]
 #   pi_url=row[4]
    print titles, price,selas


"""
pric='태연겨울'
#try:    #插入数据
cursor.execute("insert into sj (titles, price,selas,url,pi_url) values ('%s','%s','%s','%s','%s')"%(pric,'pric2','pric3','pric4','pric5'))

print "已成功插入数据>>>"
#except:
  # print "插入数据失败!!!"
time.sleep(1)

try:    #插入数据
    cursor.execute("delete from s where titles ")
    print "已成功删除数据>>>"
except:
    print "删除数据失败!!!"
   # 发生错误时回滚
  #  db.rollback()
"""
# 关闭数据库连接
db.commit()     #必须调用commit函数，否者你对数据库的所有操作将会失效！当断开连接时，所有悬挂的修改将会被重置。这很容易导致出错
db.close()

