# coding=utf-8
import urllib
import sys
import time
def report(count, blockSize, totalSize):
  percent = int(count*blockSize*100/totalSize)
  sys.stdout.write("\r%d%%" % percent + ' complete')
  sys.stdout.flush()
start=time.time()
sys.stdout.write('\rFetching ' + "pyauto-master.zip" + '...\n')
urllib.urlretrieve('https://codeload.github.com/yorkoliu/pyauto/zip/master', "pyauto-master.zip", reporthook=report)
sys.stdout.write("\rDownload complete, saved as %s" % ("pyauto-master.zip") + '\n\n')
sys.stdout.flush()
total_time = time.time() - start
print(u"总共耗时：%f 秒" % total_time)

