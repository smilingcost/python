#coding=utf-8
import requests
import time
import os


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
def auto_down(file_name,file_path,r,start):
    try:

        print r.status_code        #返回响应状态码
        r.raise_for_status()         #抛出异常
        with open(file_path, "wb") as code:
          code.write(r.content)
        total_time = time.time() - start
        print file_name,u"总共耗时：%f 秒" % total_time
       # time.sleep(0.5)
    except :
        print 'url解析错误，将重新进行下载>>>'
        time.sleep(0.5)
        afree(url)
def afree(url):
 try:
    start=time.time()
    r = requests.get(url,timeout=4) #设置超时时间，防止程序假死
    list_name = url.split('/')       #分片
    file_name = list_name[len(list_name)-1]     #取最后一个字符串
    path="D:\\meinv\\afree"
    file_path='%s/%s'%(path,file_name)
    if not os.path.exists(path):           #判断路径是否存在，不存在
     os.makedirs(path)
    auto_down(file_name,file_path,r,start)
 except:
     pass
if __name__=='__main__':
  print "开始下载文件>>>>>\n"
  for i in range(1234 ,5000):
    url = 'http://live-hls-korea-cf.afreecatv.com/livestream-12/1280x720/194348167-flash-original-hls_'+str(i)+'.ts'
    afree(url)
  print '文件下载完成'