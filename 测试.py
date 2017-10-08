#coding=utf-8

import os
import json
import re
import requests
import demjson
from lxml import etree
import lxml.html
import time
import MySQLdb
import urllib
import multiprocessing
import threading

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
header = { "User-Agent" :USER_AGENT  }

s_name='数据分析'
data=urllib.quote(s_name)       #将中文转为url编码格式

%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90
%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590
print data