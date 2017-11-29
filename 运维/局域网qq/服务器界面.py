#!/usr/bin/env python
# -*- coding:utf-8 -*-

import wx
from ChatFrame import *


class MainFrame(wx.Frame):

    """docstring for MainFrame"""

    def __init__(self, parent, ID, title):
        super(MainFrame, self).__init__(
            parent, ID, title, wx.DefaultPosition, size=(380, 600))

        self.listenThread = None

        # 界面构建
        self.Center()
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, 'port:', pos=(16, 20))
        self.portText = wx.TextCtrl(panel, -1, '3000', pos=(60, 16))
        self.openServerBtn = wx.Button(panel, -1, 'Open', pos=(160, 16))

        self.listCtrl = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.listCtrl.SetPosition((16, 80))
        self.listCtrl.SetSize((300, 400))
        self.listCtrl.InsertColumn(0, 'ID')
        self.listCtrl.InsertColumn(1, 'Name')
        self.listCtrl.SetItemCount(100)

        # 事件绑定
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.openServerBtn)

    def OnOpen(self, event):
        '''打开或关闭服务器'''
        if self.openServerBtn.Label == 'Open':
            self.openServerBtn.SetLabel('Close')
            # 启动socket线程
            self.listenThread = ListenClient(self)
            self.listenThread.start()
        else:
            self.openServerBtn.SetLabel('Open')
            # 退出socket线程
            # 退出while循环
            self.listenThread.listSocket = []
            #触发异常退出socket线程
            self.listenThread.tcpServer.shutdown(socket.SHUT_RDWR)
            self.listenThread = None

    def OnClose(self, event):
        '''程序退出'''
        if self.listenThread:
            self.listenThread.listSocket = []
            self.listenThread.tcpServer.shutdown(socket.SHUT_RDWR)
        sys.exit()

    def refreshListView(self, list):
        '''刷新好友列表'''
        self.listCtrl.DeleteAllItems()
        i = 0
        for name in list:
            self.listCtrl.InsertStringItem(i, str(i))
            self.listCtrl.SetStringItem(i, 1, name)
            i += 1


class ServerApp(wx.App):

    """wxPython的App"""

    def OnInit(self):
        frame = MainFrame(None, -1, 'Server')
        frame.Show()
        return True

if __name__ == '__main__':
    app = ServerApp(0)
    app.MainLoop()