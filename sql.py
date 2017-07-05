# -*- coding:utf-8 -*-

import pymssql

#数据库服务器信息
server="信息部"
user="sa"
password="zjg123"
database="sipei"

conn=pymssql.connect(server,user,password,database)
inStr2 = inStr.decode('utf-8', 'ignore')
cur = conn.cursor()
sql = "select * from 17lx"
cur.execute(sql)
rows = cur.fetchall()
conn.close()
for row in rows:
    print row[0]