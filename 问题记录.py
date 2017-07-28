#coding=utf-8
import cookielib

print u'连接mssql数据库编码问题导致数据无法写入数据库'


print u'爬虫是遇到编码问题导致乱码或者是爬到的网页显示为空，例如网页韩语euc kr编码导致爬取不到代码'
"""   解决：增加请求头"""

print u'编码问题导致数据无法写入本地'
""" 解决：s="数据".encode('utf-8'),s="数据"为unicode 编码，写入本地默认为gbk编码，故先将编码为，只限制于用正则，lxml获取到的数据，
         如names=re.findall(r'"bj_nick": "(.*?)",',docs)[0].encode('utf-8')），若直接是names='금화S2',则不用转化"""





