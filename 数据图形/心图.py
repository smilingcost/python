#coding=utf-8
from time import sleep
a= int(input("输入一个数: "))
b=a*4-3
left= 30
print '\033[5;30;47m'    #设置颜色
for num in range(0,a):
    print(' '*(left-num*2)+'*'+' '*num*4+'*'+' '*(b-num*4)+'*'+' '*num*4+'*')   #上半部，一行4颗*
    sleep(0.1)                      #延迟时间
for c in range(0,2*a-1):
    mum=a-c
    print(' '*(left-mum*2+2)+'*'+' '*(mum*4+b-2)+'*')  #下半部，2颗星
    sleep(0.1)
print ' '*(left+2*a)+'*'
print '输'; sleep(0.5);print '出';sleep(0.5);print '完';sleep(0.5);print '毕'