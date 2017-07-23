#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101',periods=6)
print dates                    #使用传递的numpy数组创建数据帧,
print '-'*100

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('aBCD'))
print df                       #然后使用日期索引和标记列.
print '-'*100

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                   'F' : 'foo' })
print df2             #使用传递的可转换序列的字典对象创建数据帧.
print '-'*100

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()    #同个日期有多个数据的，采用数组累加，得到唯一的数值
ts.plot() #导入matplotlib.pyplot库，绘图后再调用matplotlib.pyplot.show()方法就能把绘制的图显示出来了！
plt.show()

df3 = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
               columns=['A', 'B', 'C', 'D'])
df3 = df3.cumsum()
df3.plot(); plt.legend(loc='best')
plt.show()       #绘图