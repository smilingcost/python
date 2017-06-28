# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
mu = 2  #均值
sigma = 32  #标准差

                          #创建一个50个元素的数组，收尾与均值相差三个标准差
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50) 

                            #根据正太分布的公式写出y
y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)

                            #以x，y为横纵坐标，'r-'表示红色线，'ro-表示红色线加原点'，linewidth为线的粗细度
                            #plot.plot(x, y, 'ro-', linewidth=2)

                              #或者也可以：用'go'表示绿色原点，markersize为原点大小
plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)

                              #有灰色格子
plt.grid(True)

                               #画出来吧，少年！
plt.show()