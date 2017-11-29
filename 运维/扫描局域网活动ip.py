#coding=utf-8

import platform
import sys
import os
import time
import thread
import socket

def get_os():
  '''''
  get os 类型
  '''
  os = platform.system()
  if os == "Windows":
    return "n"
  else:
    return "c"

def ping_ip(ip_str):
  global count
  cmd = ["ping", "-{op}".format(op=get_os()),
      "1", ip_str]
  output = os.popen(" ".join(cmd)).readlines()
  try:
    ip_name = socket.gethostbyaddr(ip_str)  #返回指定ip的计算机名称
  except:
    ip_name=False
  flag = False
  for line in list(output):
    if not line:
      continue
    if str(line).upper().find("TTL") >=0:
      flag = True
      break
  if flag:
      if ip_name:
        count+=1
        print "ip: %s is ok ***and name is %s"%(ip_str,ip_name[0].encode('utf-8'))
        print u"局域网共有%s台活动电脑"%count
        print  '-------------------------------------'
def find_ip(ip_prefix):
  '''''
  给出当前的127.0.0 ，然后扫描整个段所有地址
  '''
  for i in range(1,256):
    ip = '%s.%s'%(ip_prefix,i)
    thread.start_new_thread(ping_ip, (ip,))
    time.sleep(0.3)

if __name__ == "__main__":
  print "start time %s"%time.ctime()
  count=0
  #commandargs = sys.argv[1:]  #sys.argv[]说白了就是一个从程序外部获取参数的桥梁,获取cmd里（python 扫描局域网活动ip.py 192.168.1.114）相当于数组[扫描局域网活动ip.py, 192.168.1.114]
  commandargs='192.168.1.114'
  args = "".join(commandargs)

  ip_prefix = '.'.join(args.split('.')[:-1])
  find_ip(ip_prefix)
  print "end time %s"%time.ctime()

"""
E:\tae\python代码>python 测试2.py 192.168.1.114 就会扫描 1-255所有的ip地址了

 """