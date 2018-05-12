#coding=utf-8
import requests
import time
import os
import multiprocessing

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.3228.1 Safari/537.36'
header = { "User-Agent" :USER_AGENT  }


def auto_down(file_name,file_path,r,start,url):
    try:
        print r.status_code        #返回响应状态码
        r.raise_for_status()         #抛出异常
        with open(file_path, "wb") as code:
          code.write(r.content)
        total_time = time.time() - start
        print file_name,u"总共耗时：%f 秒" % total_time
        time.sleep(3.8)
    except(Exception),e :
        print e, 'url解析错误，将重新进行下载>>>'
        time.sleep(2)
        afree(url)   #多线程时，进行回调函数时url会出现问题(url返回时已变为下个进程的统一资源定位器，不会对错误url进行重新下载，直接进入下个url），故auto_down函数增加变量url进行url变量传递回调


def afree(url):
 try:
    start=time.time()
    r = requests.get(url,headers = header)#,timeout=3) #设置超时时间，防止程序假死，即超过时间时执行下次循环
    list_name = url.split('/')       #分片
    file_name = 'd'+list_name[len(list_name)-1]     #取最后一个字符串
    path="D:\\meinv\\afree\\20180425"
    file_path='%s/%s'%(path,file_name)
    if not os.path.exists(path):           #判断路径是否存在，不存在
       os.makedirs(path)
    auto_down(file_name,file_path,r,start,url)
 except:
     pass
if __name__=='__main__':

    pool = multiprocessing.Pool(processes = 30)     #processes = 3为进程数量
    for i in range(0 ,3000):

       url = 'http://183.111.26.106/video/_definst_/mp4:vod/20180425/584/EF5C912E_203109584_4.mp4/media_'+str(i)+'.ts'
       pool.apply_async(afree, (url, ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print "开始下载文件>>>>>\n"
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print '文件下载完成'

