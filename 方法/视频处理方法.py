#coding=utf-8


import os
import json
import re
#视频合并
path='D:/meinv/afree/1.mp4'
f=open(path,'wb')
for i in range(0,14):
    file='media_w613069317_'+str(i)+'.ts'
    path1='D:/meinv/afree/20171114/1/'+file
    f1=open(path1,'rb')           #  要读取二进制文件，比如图片、视频等等，用’rb’模式打开文件即可
    data=f1.read()
    f1.close()
    f.write(data)
    print '成功合并了文件：',file
f.close()



import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize

fps = 24   #视频帧率
fourcc=VideoWriter_fourcc(*"MJPG")
videoWriter = cv2.VideoWriter('D:/meinv/afree/2.mp4', fourcc, fps,(1360,480))   #(1360,480)为视频大小
for i in range(1,10):
 #   p1='media_w613069317_0'
    p2=i

    img12 = cv2.imread('D:/meinv/afree/20171114/1/'+'media_w613069317_'+str(p2)+'.ts')
#    cv2.imshow('img', img12)
#    cv2.waitKey(1000/int(fps))
    videoWriter.write(img12)
videoWriter.release()



from moviepy.editor import *
#视频剪切
# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60负载myholidays.mp4选择子片段
clip = VideoFileClip(u"C:/Users/Administrator/Desktop/辅助管理及GSP管理.wmv").subclip(50,60)

# Generate a text clip (many options available ! )生成文本剪辑（许多可用的选项）
#txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
#txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip above the first clip在第一个剪辑上方覆盖文本剪辑
#final_clip = CompositeVideoClip([clip])

# write the result to a file in any format以任何格式将结果写入文件
clip.to_videofile("myHolidays_edited.avi",fps=25, codec='mpeg4')