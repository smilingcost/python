#coding=utf-8

import pymssql
import time
import sys
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def fx():
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
    info=cursor.fetchall()[0:10]
    print info
    tim=[]
    sl=[]
    i=0
    for a in info:
       t=info[i][0]
       s=info[i][1]
       tim.append(t)
       sl.append(s)
       i+=1
    date=pd.DataFrame(sl,index=tim,columns=['sl'])
    date.plot(kind='bar')
    plt.show()

def fx1():
    cursor.execute("""select cp.show_name ,
 sum(a.saleCount) as s
from oa_crm_whFlow a
left join rs_ygb s on s.YGBH=a.manager
left join oa_crm_wellHospital w on w.whId=a.whid
left join OA_CRM_DZCPFWXX cp on cp.cpbh=a.cpbh
where isnull(a.org_id,1)=1 and isnull(a.enable,1)=1
      and a.exp_date>='2017-01-01' and a.saleCount>'1000'
group by a.exp_date,cp.show_name

                      """)      #使用三引号的字符串来多行分解,
#语句不能出现中文，不能用order by

#如果update/delete/insert记得要conn.commit()
 #否则数据库事务无法提交
    info=cursor.fetchall()
    print info
    tim=[]
    sl=[]
    i=0
    for a in info:
       t=info[i][0].encode("ISO-8859-1").encode("utf-8")
       print t
       s=info[i][1]
       tim.append(t)
       sl.append(s)
       i+=1
    date=pd.DataFrame(sl,index=tim,columns=['sl'])
    date=date.cumsum()
    ax=date.plot(kind='bar',title=u"17年产品销量")
    labels = ax.get_xticklabels()+ax.legend().texts+[ax.title]   #中文标签显示
    for label in labels :
      label.set_fontproperties(font)    #中文标签显示
    plt.show()

if __name__ == '__main__':
    #数据库服务器信息
    conn  = pymssql.connect(server="192.168.1.193", user="sa", password="***", database="ren",charset="ISO-8859-1")  #用此语句连接，获得连接对象。charset="ISO-8859-1"根据每台电脑实际设置
    cursor = conn.cursor()  # %获得游标。
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  #中文标签显示
    fx()
 #   fx1()
