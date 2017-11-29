# -*- coding: cp936 -*-
#coding=utf-8
import os
import re
import thread
import time
import socket
import sys

def Ping_Ip(Curr_Ip):

    global Count_Thread,lock,ThreadsNum

    #print "*****************Chile_Thread-Begin****************"+"\n"

    ping_cmd = "ping" +" "+Curr_Ip


    Ping_Answer = os.popen(ping_cmd).readlines()
    patt = r'TTL=([0-9]{2})'
    TTL_Str=re.findall(patt,Ping_Answer[2])

    if len(TTL_Str) == 0:
        #print Curr_Ip+"is Not Alive"
        pass
        #print "*****************Chile_Thread-Over****************"+"\n"
    else:
        try:
          HostInfo = socket.gethostbyaddr(Curr_Ip)
          Mac_address=Get_Mac_Addr(Curr_Ip)
        except:
          HostInfo=False
          Mac_address=False
        #print "Mac_address"+Mac_address
        if HostInfo:
            if Mac_address:
               print "\n"+"Alive Host----->   "+"HostComputerName:"+HostInfo[0]+"   Mac_address:"+Mac_address+"\t"+"Ip:"+Curr_Ip

        #print "*****************Chile_Thread-Over****************"+"\n"


    lock.acquire()
    Count_Thread = Count_Thread+1
    if Count_Thread ==ThreadsNum:
        print "*****************NetWork_End***************"
    lock.release()



def Get_Mac_Addr(Curr_Ip):

    Mac_cmd = "nbtstat -A "+Curr_Ip
    Mac_Info = os.popen(Mac_cmd).readlines()

    Mac_Info_Sum=""

    for index in range(0,len(Mac_Info)):
        Mac_Info_Sum=Mac_Info_Sum+Mac_Info[index]


    patt_mac = r'= (.{2}-.{2}-.{2}-.{2}-.{2}-.{2})'
    mac_addr= re.findall(patt_mac,Mac_Info_Sum)
    return mac_addr[0]



def GetAliveIp(Net_iP_Init,IpBegin,IpEnd):
    SplitIp = Net_iP_Init.split(".")
    Ip1=SplitIp[0]
    Ip2=SplitIp[1]
    Ip3=SplitIp[2]

    Prefix_Ip = Ip1+"."+Ip2+"."+Ip3+"."


    for Ip_Last in range(IpBegin,IpEnd+1):
        Curr_Ip=Prefix_Ip+str(Ip_Last)

        thread.start_new_thread(Ping_Ip, (Curr_Ip,))
        time.sleep(2)



def GetNetGate():
    Netgate_cmd = "ipconfig /all"
    Netgate_info = os.popen(Netgate_cmd).readlines()

    Netgate_info_Str = ""
    for index in range(0,len(Netgate_info)):
        Netgate_info_Str=Netgate_info_Str+Netgate_info[index]
    print Netgate_info_Str
        #print type(Netgate_info_Str)

    patt_hn = r'主机名  . . . . . . . . . . . . . : (.+)'
    Host_Name_Local = re.findall(patt_hn,Netgate_info_Str)

    Rent_Ip_Begin=r'获得租约的时间  . . . . . . . . . : (.+)'
    Rent_Ip_Begins=re.findall(Rent_Ip_Begin,Netgate_info_Str)

    Rent_Ip_End=r'租约过期的时间  . . . . . . . . . : (.+)'
    Rent_Ip_Ends=re.findall(Rent_Ip_End,Netgate_info_Str)

    patt_ipv6 = r'本地链接 IPv6 地址. . . . . . . . : ([a-z0-9]{3,4}::[a-z0-9]{3,4}:[a-z0-9]{3,4}:[a-z0-9]{3,4}:[a-z0-9]{3,4}%[0-9]{2})'
    ipv6 = re.findall(patt_ipv6,Netgate_info_Str)

    patt_ipv4 = r'IPv4 地址 . . . . . . . . . . . . : ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})'
    ipv4 = re.findall(patt_ipv4,Netgate_info_Str)

    YanMas= r'子网掩码  . . . . . . . . . . . . : ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})'
    YM = re.findall(YanMas,Netgate_info_Str)

    Netgates = r'默认网关. . . . . . . . . . . . . : ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})'
    Ng = re.findall(Netgates,Netgate_info_Str)

    Patt_dhcp = r'DHCP 已启用 . . . . . . . . . . . : (.{1,2})'
    dhcp_Is=re.findall(Patt_dhcp,Netgate_info_Str)

    Patt_dhcp_server = r'DHCP 服务器 . . . . . . . . . . . : ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})'
    dhcp_server = re.findall(Patt_dhcp_server,Netgate_info_Str)

    print "本地主机名:  "+Host_Name_Local[0]
    print "本机IPv6地址:  "+ipv6[0]
    print "本机IPv4地址:  "+ipv4[0]
    print "子网掩码:  "+YM[0]
    print "默认网关:  "+Ng[0]
    print "是否启用DHCP:  "+dhcp_Is[0]
    print "DHCP服务器IP:  "+dhcp_server[0]
    print "动态租约起始时间:  "+Rent_Ip_Begins[0]
    print "动态租约过期时间:  "+Rent_Ip_Ends[0]

    return Ng[0]


if __name__ == "__main__":

    Count_Thread = 0
    lock = thread.allocate_lock()
    print "*****************NetWork_Begin**************"

    Net_iP_Init=GetNetGate()

    IpBegin = raw_input("请输入侦听起始IP:")
    IpEnd = raw_input("请输入侦听结束IP:")

    IntIpBegin = int(IpBegin)
    IntIpEnd = int(IpEnd)

    ThreadsNum = IntIpEnd+1-IntIpBegin

    GetAliveIp(Net_iP_Init,IntIpBegin,IntIpEnd)

