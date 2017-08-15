#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import demjson
import json
#import simplejson as json

f=open(u"爬虫\\淘宝_js-m\\sj.csv")
r=f.read().encode("utf-8")
print r
