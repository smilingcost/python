#coding=utf-8
import os

def wget(ml):
    print '输入命令：',ml
    mystr=os.popen(ml)  #popen与system可以执行指令,popen可以接受返回对象
    mystr=mystr.read() #读取输出
    print '运行结果：',mystr.encode('utf-8')

if __name__=='__main__':
    #ml="wget.exe --help"
    ml='wget.exe http://sw.bos.baidu.com/sw-search-sp/software/a988efebbc8e0/QQ_9.0.1.23153_setup.exe'
    wget(ml)