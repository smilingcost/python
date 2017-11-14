#coding=utf-8

from moviepy.editor import *


for i in range(0,975):
  try:
    file='media_w1215728150_'+str(i)+'.ts'
    path1='D:/meinv/afree/20171114/3/'+file
    clip = VideoFileClip( path1)
    final_clip = CompositeVideoClip([clip])
# write the result to a file in any format以任何格式将结果写入文件
    final_clip.to_videofile("D:/meinv/afree/4.mp4",fps=25, codec='mpeg4')
    print '成功合并了文件：',file
  except:
      print '视频不存在'
      pass

  imageio.plugins.ffmpeg.download()