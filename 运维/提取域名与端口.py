#coding=utf-8

import urllib
proto, rest = urllib.splittype("http://14.23.146.99:93/login.jre")
host, rest = urllib.splithost(rest)
print host
host, port = urllib.splitport(host)
if port is None:
   port = 80
print port