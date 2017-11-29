#!/usr/bin/env python
# -*- coding:utf-8 -*-

import wx
import socket
import threading
import select
import fcntl
import struct
import sys
import random

# 获取本地IP


def get_ip_address(ifname):
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print skt
    pktString = fcntl.ioctl(
        skt.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
    print pktString
    ipString = socket.inet_ntoa(pktString[20:24])
    return ipString


class ListenClient(threading.Thread):

    """Socket 线程"""

    def __init__(self, frame):
        threading.Thread.__init__(self)
        # 用字典来存储客户端的信息，key:客户端的名字,value:客户端的IP地址
        self.clientInfo = {}
        # 服务器界面frame
        self.frame = frame

    def run(self):
        '''线程执行的程序'''
        self.buildServer()

        while self.listSocket:
            #有数据可读的时候，select返回(可能描述不是很准确)
            rlist, wlist, elist = select.select(self.listSocket, [], [])
            if not (rlist or wlist or elist):
                print 'time out'
                break
            for sock in rlist:
                #如果是tcpServer表示有新的客户端向我们发送连接请求了
                if sock is self.tcpServer:
                    print 'connecting ...'
                    try:
                        client, addr = sock.accept()
                        print 'connect from', addr
                        client.setblocking(False)
                        #将新的客户端添加到listSocket,这样就可以被select检测了
                        self.listSocket.append(client)
                    except Exception, e:
                        print 'exit threading'
                        break
                elif sock is self.udpServer:
                    #udp　表示用户发送的聊天消息
                    data, addr = sock.recvfrom(1024)
                    print 'recvfrom ', data, ' from', addr
                    #将消息发送到所以客户机上，转发
                    for key, value in self.clientInfo.items():
                        sock.sendto(data, value)
                else:
                    #tcpClient　就是客户端发送的命令
                    command = sock.recv(1024)
                    print 'command:', command
                    #当command 为空的时候　表示客户端tcp已经断开连接了
                    if command:
                        self.parse(command)
                    else:
                        self.listSocket.remove(sock)

        print 'out threading'
        self.tcpServer.close()

    def buildServer(self):
        '''服务器端口绑定'''
        print 'launch threading'
        # tcp服务器建立
        self.tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpServer.setblocking(False)
        self.tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        localIP = get_ip_address('wlan0')
        serverPort = int(self.frame.portText.Value)
        # 服务器地址绑定
        self.tcpServer.bind((localIP, serverPort))
        self.tcpServer.listen(0)
        # udp的端口是tcp端口号+1
        self.udpPort = serverPort + 1
        self.udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpServer.bind((localIP, self.udpPort))
        self.udpServer.setblocking(False)

        # select 输入可读参数，意思是当这个列表里面任何一个元素可读，select就有返回值
        self.listSocket = [self.tcpServer, self.udpServer]

    def sendListName(self):
        '''向客户端发送在线好友列表'''
        listName = 'listName:'
        for name in self.clientInfo:
            listName += name + ';'
        print listName
        count = len(self.listSocket)
        for i in range(2, count):
            self.listSocket[i].sendall(listName)

    def refreshListView(self):
        '''更新在线好友列表'''
        wx.CallAfter(self.frame.refreshListView, self.clientInfo)

    def parse(self, command):
        '''解析命令'''
        key, value = command.split(':')
        if key == 'connectInfo':
            name, addr = value.split(',')
            print name, addr
            host, port = addr.split('%')
            self.clientInfo[name] = (host, int(port))
            print self.clientInfo
            self.sendListName()
            self.refreshListView()
        if key == 'exit':
            del self.clientInfo[value]
            self.sendListName()
            self.refreshListView()