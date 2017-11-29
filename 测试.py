#coding=utf-8


import platform
import sys
import os
import time
import thread
import socket
def find_ip(ip_prefix):
  '''''
  给出当前的127.0.0 ，然后扫描整个段所有地址
  '''
  for i in range(1,256):
    ip = '%s.%s'%(ip_prefix,i)
    print ip
    time.sleep(0.3)
commandargs = sys.argv[1:]
args = "".join(commandargs)
ip_prefix = '.'.join(args.split('.')[:-1])
find_ip(ip_prefix)




