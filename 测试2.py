#coding=utf-8
import requests
import time
import os
import multiprocessing
import re

im='static/img/qh/(1).gif'
nid=re.findall(r'static/img/qh/\((.*?)\).gif',im)[0]
print nid
