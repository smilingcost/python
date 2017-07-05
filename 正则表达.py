# coding: utf-8
import re
x=re.findall('w{3}\.([a-zA-Z]+\.)+com','www.baidu.com')
y=re.findall('www\.([a-zA-Z]+\.)+com','www.baidu.com')
z=re.findall('(?<=[(])[^()]+\.[^()]+(?=[)])','Job stream (http://www.cnpythoner.com)(0AA.AAAAAAAAAJULH) has completed successfully.')
z1=re.findall('([A-Z]+)\|([a-z]+)',"var station_names ='@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|BJP|beijing|bj|2'")
   #组成多个元祖,[（大写，小写）]
z2=re.findall('\#([a-z0-9]*)', "[u'#', u'#', u'#', u'#id4', u'#id7', u'#id8', u'#id11', u'#id12', u'#id13']")
z3=re.findall('(https(.*?)type=)','https://www.douban.com/doulist/1264675/?start=25&sort=seq&sub_type=')
print 'x',x
print 'y',y
print 'z',z
print 'z1',z1
print 'z2',z2   #（）里的为分组，输出的为（）的内容其他的不输出
print 'z3',z3   #.*具有贪婪的性质，首先匹配到不能匹配为止，根据后面的正则表达式，会进行回溯。
                  #.*？则相反，一个匹配以后，就往下进行，所以不会进行回溯，具有最小匹配的性质。