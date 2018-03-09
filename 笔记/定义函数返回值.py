#coding=utf-8
from time import sleep
num = 1
def cu(lst = [num]):
    if len(lst) > 3:
        lst.pop(0)            #移除元素并返回该值
    yield lst                #相当于return
    lst.append(lst[-1] + 1)   #列表末添加一个元素,lst[-1]为返回lst最后一个元素
a=int(input('执行次数： '))
for i in range(a):             #a是你想执行的次数
    for line in cu():
        for j in line:
            print(j)
    print('================')
    sleep(1)