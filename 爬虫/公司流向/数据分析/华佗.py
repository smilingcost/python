#coding=utf-8

import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False   #用来正常显示负号

def main1():
  ht=pd.read_csv(u'华佗.csv')[0:10]
  x = []
  y1 = []
  y2 = []
  for xs,ys1,ys2 in zip(ht["hos"],ht["2016"],ht["2017"]):   #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        x.append(str(xs))
        y1.append(float(ys1))
        y2.append(float(ys2))
  ht1=pd.DataFrame(zip(y1,y2) ,index=x)
  print ht1
  ht1.plot.bar()  # ht1.plot(kind='bar')
  plt.title(u'2016年华佗')
  plt.xlabel(u'销量')
  plt.ylabel(u'医院')
  plt.show()

def main2():
  ht=pd.read_csv(u'华佗.csv')[0:10]
  x = []
  y1 = []
  for xs,ys1 in zip(ht["hos"],ht["2016"]):   #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        x.append(str(xs))
        y1.append(float(ys1))

  ht1=pd.DataFrame(y1 ,index=x)
  print ht1
  ht1.plot.pie(subplots=True,autopct = '%3.1f%%')  # ht1.plot(kind='bar')
  ##autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
  plt.title(u'2016年华佗')
  plt.xlabel(u'销量')
  plt.ylabel(u'医院')
  plt.show()

def main3():
  ht=pd.read_csv(u'华佗.csv')
  x = []
  y1 = []
  for xs,ys1 in zip(ht["ywy"],ht["2016"]):   #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        x.append(str(xs))
        y1.append(float(ys1))

  ht1=pd.DataFrame(zip(x,y1) ,index=x,columns=["x","y1-2016"])
  ht2=ht1.groupby("x").sum()      #合并
  ht3=ht2.sort_values(by='y1-2016')    #排序
  print ht3
  ht2.plot.bar()  # ht1.plot(kind='bar')
  #设置数字标签*
  plt.title(u'2016年华佗')
  plt.xlabel(u'业务员')
  plt.ylabel(u'销量')
  plt.xticks(rotation=30,fontsize=10)  #旋转和字体大小
  plt.show()

if __name__ == '__main__':
    #main1()
   # main2()
    main3()