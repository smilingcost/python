#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tb=pd.read_csv('sj.csv')             #读取文本
df=pd.DataFrame(tb,columns=['price'])          #获取指定列
tb_s=np.where(df>6000,1,np.where(df>4000,2,3))    #将价格划分为3个等级

i=0
tb1_1=[]
for aa in tb_s:            #将多维数组的值取出来放到列表中
    x=tb_s[i,0]
    tb1_1.append(x)
    i+=1
tb1s=pd.DataFrame(tb,columns=['price','selas'])
data={'price_level':tb1_1}
tb_i=pd.DataFrame(data)             #创建价格等级数组
tb1_1=pd.concat([tb1s, tb_i],axis=1)                #concat合并数组，axis=1按列合并
tb1_2=tb1_1['price'].groupby(tb1_1['price_level']).mean()       #分组聚合
tb1_3=tb1_1['selas'].groupby(tb1_1['price_level']).mean()
print tb1_1
print
print tb1_2,tb1_3
tb1s.plot()
plt.show()
