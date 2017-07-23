#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(u"E:\\文件\\招商协议\\前列通.csv")   #有中文路径的要加u
print type(df)
# 输出：<class 'pandas.core.frame.DataFrame'> 可见读取后变成一个DataFrame变量
print df.head(5)
