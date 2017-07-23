#coding=utf-8
import requests
import time
import os
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
print "开始下载文件>>>>>\n"

for i in range(1458,10000):
   start=time.time()
   url = 'http://live-hls-korea-cf.afreecatv.com/livestream-22/1280x720/194241689-flash-original-hls_'+str(i)+'.ts'
   list_name = url.split('/')
   file_name = list_name[len(list_name)-1]
   path="D:\\meinv\\afree"
   file_path='%s/%s'%(path,file_name)
   if not os.path.exists(path):           #判断路径是否存在，不存在
     os.makedirs(path)
   r = requests.get(url)
   with open(file_path, "wb") as code:
     code.write(r.content)
   total_time = time.time() - start
   print file_name,u"总共耗时：%f 秒" % total_time
print '文件下载完成'