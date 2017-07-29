# coding=utf-8
import urllib
import sys
import time
def report(count, blockSize, totalSize):
  percent = int(count*blockSize*100/totalSize)
  sys.stdout.write("\r%d%%" % percent + ' complete')
  sys.stdout.flush()
start=time.time()
sys.stdout.write('\rFetching ' + "python2.7.zip" + '...\n')
urllib.urlretrieve('http://pcr1.pc6.com/rm/python2.7.zip', "python2.7.zip", reporthook=report)
sys.stdout.write("\rDownload complete, saved as %s" % ("python2.7.zip") + '\n\n')
sys.stdout.flush()
total_time = time.time() - start
print(u"总共耗时：%f 秒" % total_time)

