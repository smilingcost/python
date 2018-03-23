# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
# 这里注意：1:2其实只有第一列，与1 的区别是这表示的是一个matrix矩阵，而非单一向量。
y = dataset.iloc[:, 2].values

poly_reg = PolynomialFeatures(degree = 4) #degree 就是自变量需要的维度,degree=1 意思是自变量只有一次，相当于简单线性回归
X_poly = poly_reg.fit_transform(X)      #fit_transform,fit找到数据转换规则，并将数据标准化
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# 图像中显示
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))  #通过拆分横坐标将图像变得平滑一些:
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

x=lin_reg_2.predict(poly_reg.fit_transform(6)) #下面我们给出一个测试值来试试结果 （6,10）
y=lin_reg_2.predict(poly_reg.fit_transform(11))
print x,y