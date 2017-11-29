#!/usr/bin/env python
# -*- coding:utf-8 -*-

import wx
from ChatFrame import *


class MainFrame(wx.Frame):

    """Chat的聊天主界面"""

    def __init__(self, parent, ID, title):
        super(MainFrame, self).__init__(
            parent, -1, title, wx.DefaultPosition, wx.Size(640, 480))
        self.Center()
        self.name = title
        panel = wx.Panel(self, -1)
        #界面的创建
        #聊天内容文本框
        self.chatContext = wx.TextCtrl(
            panel, -1, '', size=(500, 360), style=wx.TE_MULTILINE | wx.TE_READONLY)
        #发送消息文本框
        self.sendText = wx.TextCtrl(
            panel, -1, size=(500, 80), style=wx.TE_MULTILINE)
        self.sendText.SetPosition((0, 370))
        #在线好友列表
        self.listClient = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.listClient.SetSize((120, 480))
        self.listClient.SetPosition((510, 0))
        self.listClient.InsertColumn(0, 'ID')
        self.listClient.InsertColumn(1, 'Name')
        #按钮
        self.sendBtn = wx.Button(panel, -1, 'Send', pos=(300, 450))
        self.exitBtn = wx.Button(panel, -1, 'Exit', pos=(410, 450))
        #事件绑定
        self.Bind(wx.EVT_BUTTON, self.OnSendMessage, self.sendBtn)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnSendMessage(self, event):
        '''发送消息'''
        print 'sendMessage'
        self.chat.sendMessage(self.name + ':' + self.sendText.Value)

    def connect(self, addr):
        '''给登录界面判断是否连接成功'''
        self.chat = Chat(self)
        if self.chat.connect(addr):
            self.chat.start()
            return True
        else:
            return False

    def refreshListView(self, listName):
        '''刷新在线好友列表'''
        self.listClient.DeleteAllItems()
        i = 0
        for name in listName:
            self.listClient.InsertStringItem(i, str(i))
            self.listClient.SetStringItem(i, 1, name)
            i += 1

    def appendMsg(self, msg):
        '''追加接收到消息'''
        self.chatContext.AppendText(msg + '\n')

    def OnClose(self, event):
        '''程序退出'''
        self.chat.sendExit()
        self.chat.listSocket = []
        self.chat.tcpSocket.shutdown(socket.SHUT_RDWR)
        sys.exit()