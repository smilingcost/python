# -*- encoding:utf-8 -*-
import MySQLdb
import time
from numpy.random import randn
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import pandas.io.sql as sql

# 打开数据库连接
<<<<<<< HEAD
db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="***",db="tbgoods",charset="utf8") #将localhost改为127.0.0.1，不然出错
=======
db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="*&*",db="tbgoods",charset="utf8") #将localhost改为127.0.0.1，不然出错
>>>>>>> origin/master
date=sql.read_sql('SELECT *   from tb_pl',db)      #将数据库中的数据表自动导入DataFrame
print date
