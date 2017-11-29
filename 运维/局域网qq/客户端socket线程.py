#!/usr/bin/env python
# -*- coding:utf-8 -*-
import wx
import fcntl
import struct
import socket
import threading
import select
import random
import sys

#获取本地地址，这里面是在Linux环境下的获取方式，windows下请百度
def get_ip_address(ifname):
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print skt
    pktString = fcntl.ioctl(
        skt.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
    print pktString
    ipString = socket.inet_ntoa(pktString[20:24])
    return ipString

#socket线程
class Chat(threading.Thread):

    """docstring for Chat"""

    def __init__(self, frame):
        super(Chat, self).__init__()
        #聊天界面frame
        self.frame = frame
        #监听连接的tcp客户端，用来发送命令
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #用于发送聊天内容的udp
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #获取本地IP地址，这里面我是使用了无线网wlan0，可以用ifconfig查看
        self.localIP = get_ip_address('wlan0')
        #产生一个随机数作为udp的端口号
        self.udpPort = random.randint(3000, 6000)
        #为udp绑定地址
        self.udpSocket.bind((self.localIP, self.udpPort))
        #select的可读入参数
        self.listSocket = [self.tcpSocket, self.udpSocket]

    def run(self):
        self.sendInfo()
        while self.listSocket:
            print 'waiting event'
            #select函数　返回self.listSocket里面可读的对象
            rlist, wlist, elist = select.select(self.listSocket, [], [])
            for sock in rlist:
                #如果是tcp　表示我们接收到是命令
                if sock is self.tcpSocket:
                    command = sock.recv(1024)
                    if command:
                        self.parse(command)
                    else:
                        break
                else:　#udp　则是我们的聊天内容
                    try:
                        data, addr = sock.recvfrom(1024)
                        self.appendMsg(data)
                    except Exception, e:
                        break
        self.tcpSocket.close()
        self.udpSocket.close()

    def connect(self, addr):
        '''给登录界面判断是否连接成功'''
        try:
            host, port = addr.split(':')
            print host, port
            self.serverTcpPort = int(port)
            self.serverUdpAddr = (host, self.serverTcpPort + 1)
            self.tcpSocket.connect((host, int(port)))
            self.tcpSocket.setblocking(False)
            print 'connect Server'
            return True
        except Exception, e:
            print "Can't connect Server"
            return False

    def parse(self, command):
        '''用于解析服务器的命令'''
        key, value = command.split(':')
        if key == 'listName':
            listName = value.split(';')
            listName.remove('')
            self.refreshListView(listName)

    def sendInfo(self):
        '''向服务器发送客户机的名称'''
        self.tcpSocket.sendall(
            'connectInfo:' + self.frame.name + ',' + self.localIP + '%'
            + str(self.udpPort))

    def sendExit(self):
        '''向服务器发送退出消息'''
        self.tcpSocket.sendall('exit:' + self.frame.name)

    def sendMessage(self, msg):
        '''给GUI调用的，表示用户向服务器发送消息'''
        self.udpSocket.sendto(msg, self.serverUdpAddr)

    def refreshListView(self, listName):
        '''刷新在线好友列表，由于是多线程所以是用wx.CallAfter,让GUI线程去执行'''
        wx.CallAfter(self.frame.refreshListView, listName)

    def appendMsg(self, msg):
        '''接收到的消息追加到聊天窗口中'''
        wx.CallAfter(self.frame.appendMsg, msg)