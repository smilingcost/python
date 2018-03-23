# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
#这里是引用了交叉验证，train_test_split将阵列或矩阵拆分成随机列和测试子集

#一次多元线性回归的预测
#例如商品的销售额可能不电视广告投入,收音机广告投入,报纸广告投入有关系,可以有 sales =β0+β1*TV+β2* radio+β3*newspaper.
data = pd.read_csv('Advertising.csv')

# display the first 5 rows
#print data.head()
# display the last 5 rows
#print data.tail()
# check the shape of the DataFrame(rows, colums)
#print data.shape

#scikit-learn要求X是一个特征矩阵，y是一个NumPy向量。
#X可以是pandas的DataFrame，y可以是pandas的Series，scikit-learn可以理解这种结构
#create a python list of feature names
feature_cols = ['TV', 'Radio', 'Newspaper']
# use the list to select a subset of the original DataFrame
X = data[feature_cols]
# equivalent command to do this in one line
X = data[['TV', 'Radio', 'Newspaper']]
# print the first 5 rows
print X.head(),'\n'
# check the type and shape of X
print type(X)
print X.shape #行列数
# select a Series from the DataFrame
y = data['Sales']
# equivalent command that works if there are no spaces in the column name
y = data.Sales
# print the first 5 values
print y.head(),'\n'
time.sleep(1)

#构建训练集与测试集
X_train,X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print X_train.shape
print y_train.shape
print X_test.shape
print y_test.shape
time.sleep(1)

#线性回归
linreg = LinearRegression()
model=linreg.fit(X_train, y_train)
print model,'\n'
print linreg.intercept_
print linreg.coef_
# pair the feature names with the coefficients
r=zip(feature_cols, linreg.coef_)
print r,'\n'   #得到各变量系数值
time.sleep(1)
"""
y=2.668+0.0464∗TV+0.192∗Radio-0.00349∗Newspaper
如何解释各个特征对应的系数的意义？
对于给定了Radio和Newspaper的广告投入，如果在TV广告上每多投入1个单位，对应销量将增加0.0466个单位。就是加入其它两个媒体投入固定，在TV广告上每增加1000美元（因为单位是1000美元），销量将增加46.6（因为单位是1000）。但是大家注意这里的newspaper的系数居然是负数，所以我们可以考虑不使用newspaper这个特征。这是后话，后面会提到的。"""

#、预测
y_pred = linreg.predict(X_test)
print y_pred
print type(y_pred),'\n'
time.sleep(1)

#1)平均绝对误差(Mean Absolute Error, MAE)
#(2)均方误差(Mean Squared Error, MSE)
#(3)均方根误差(Root Mean Squared Error, RMSE)
print type(y_pred),type(y_test)
print len(y_pred),len(y_test)
print y_pred.shape,y_test.shape
sum_mean=0
for i in range(len(y_pred)):
    sum_mean+=(y_pred[i]-y_test.values[i])**2
sum_erro=np.sqrt(sum_mean/50)
# calculate RMSE by hand
print "RMSE by hand:",sum_erro,'\n'
time.sleep(1)

#做ROC曲线
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()#（红色的线是真实的值曲线，蓝色的是预测值曲线）