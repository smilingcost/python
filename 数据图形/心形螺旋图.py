# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
t = np.linspace(0, 7, 100)
x = 16 * np.sin(t) ** 3
y = 14 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
plt.plot(x, y, 'r-', linewidth=2)
plt.grid(True)
plt.show()        #心形图

t = np.linspace(0, 50, num=1000)
x = t*np.sin(t) + np.cos(t)
y = np.sin(t) - t*np.cos(t)
plt.plot(x, y, 'r-', linewidth=2)
plt.grid()
plt.show()         # 螺旋图