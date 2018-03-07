#coding=utf-8
import subprocess
"""参数	作用
args	一般是一个字符串，是要执行的shell命令内容
bufsize	设置缓冲，负数表示系统默认缓冲，0表示无缓冲，正数表示自定义缓冲行数
stdin	程序的标准输入句柄，NONE表示不进行重定向，继承父进程，PIPE表示创建管道
stdout	程序的标准输出句柄，参数意义同上
stderr	程序的标准错误句柄，参数意义同上，特殊，可以设置成STDOUT，表示与标准输出一致
shell	为True时，表示将通过shell来执行
cwd	用来设置当前子进程的目录
env	设置环境变量，为NONE表示继承自父进程的
universal_newlines	将此参数设置为True，Python统一把这些换行符当作’/n’来处理。"""

def execute_command(cmd):
    print('start executing cmd...')
    s = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stderrinfo, stdoutinfo = s.communicate()
    print('stderrinfo is -------> %s and stdoutinfo is -------> %s' % (stderrinfo.encode('utf-8'), stdoutinfo.encode('utf-8')))
    print('finish executing cmd....')
    return s.returncode


cmd = r'wget.exe http://sw.bos.baidu.com/sw-search-sp/software/a988efebbc8e0/QQ_9.0.1.23153_setup.exe'
result = execute_command(cmd)
print 'result:------>', result
