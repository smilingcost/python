# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 50)
plt.subplot(3, 1, 1) # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')
plt.subplot(3, 1, 2)
plt.plot(x, np.cos(x), 'g')
plt.subplot(3, 1, 3)
plt.plot(x, np.tan(x), 'b')
plt.show()