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


# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-*', label='Cos(x)')
plt.legend() # 展示图例
plt.xlabel('Rads') # 给 x 轴添加标签
plt.ylabel('Amplitude') # 给 y 轴添加标签
plt.title('Sin and Cos Waves') # 添加图形标题
plt.show()


# -*- coding: cp936 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10,8))  #建立一个大小为10*8的画板
ax1 = fig.add_subplot(3,3,1)  #在画板上添加3*3个画布，位置是第1个
ax2 = fig.add_subplot(3,3,2)
ax3 = fig.add_subplot(3,3,3)
ax4 = fig.add_subplot(3,3,4)
ax5 = fig.add_subplot(3,3,5)
ax6 = fig.add_subplot(3,3,6)
ax7 = fig.add_subplot(3,3,7)
ax8 = fig.add_subplot(3,3,8)
ax9 = fig.add_subplot(3,3,9)

ax1.plot(np.random.randn(10))
ax2.scatter(np.random.randn(10),np.arange(10),color='r')  #作散点图
ax3.hist(np.random.randn(20),bins=10,alpha=0.3)  #作柱形图
ax4.bar(np.arange(10),np.random.randn(10))  #做直方图
ax5.pie(np.random.randint(1,15,5),explode=[0,0,0.2,0,0])  #作饼形图

x = np.arange(10)
y = np.random.randn(10)
ax6.plot(x,y,color='green')
ax6.bar(x,y,color='k')

data = DataFrame(np.random.randn(1000,10),
                 columns=['one','two','three','four','five','six','seven','eight','nine','ten'])
data2 = DataFrame(np.random.randint(0,20,(10,2)),columns=['a','b'])
data.plot(x='one',y='two',kind='scatter',ax=ax7)  #针对DataFrame的一些作图
data2.plot(x='a',y='b',kind='bar',ax=ax8,color='red',legend=False)
data2.plot(x='a',y='b',kind='barh',color='m',ax=ax9)
plt.tight_layout() #避免出现叠影
plt.show()



import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
menStd =   (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

# add some
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )

ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()




# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
# 彩色映射散点图
x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 5
colour = np.random.rand(1000)
plt.scatter(x, y, size, colour)
plt.colorbar()
plt.show()