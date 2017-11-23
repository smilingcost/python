#coding=utf-8

import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    authorizer.add_user('user', '12345', 'E:/tae', perm='elradfmwM')
    # authorizer.add_anonymous(os.getcwd()) #此处添加一个匿名用户

    handler = FTPHandler    #初始化处理客户端命令的类
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready." #客户端连接时返回的字符串
    #handler.masquerade_address = '151.25.42.11'  #如果你在NAT之后，就用这个指定被动连接的参数
    #handler.passive_ports = range(60000, 65535)


    address = ('192.168.1.114', 2121) #设置服务器的监听地址和端口
    server = FTPServer(address, handler)

     #给链接设置限制
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # 启动服务器
    server.serve_forever()

if __name__ == '__main__':
    main()


"""
读权限 ：

e	改变文件目录
l	列出文件
r	从服务器接收文件
写权限 ：

a	文件上传
d	删除文件
f	文件重命名
m	创建文件
w	写权限
M	文件传输模式（通过FTP设置文件权限 ）"""