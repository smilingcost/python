#coding=utf-8

import os
import json
import re
import time
#视频合并，合并视频属性必须一致，且视频不能裁剪，否则时间不准。
path='D:/meinv/afree/20171227-2.ts'
f=open(path,'wb')
for i in range(330,3000):
 try:
    file='1'+' ('+str(i)+')'+'.ts'
    path1='D:/meinv/afree/20171227/'+file
    f1=open(path1,'rb')           #  要读取二进制文件，比如图片、视频等等，用’rb’模式打开文件即可
    data=f1.read()
    f.write(data)
    f1.close()
    print '成功合并了文件：',file
   # time.sleep(0.5)      #增加时间
 except:
     pass
f.close()




