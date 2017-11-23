#coding=utf-8


import re, os

def get_ipconfig_ip():
    match_ip_dict = {}
    ipconfig_result_list = os.popen('ipconfig').readlines() #执行cmd命令ipconfig，并将结果存于ipconfig_result_list

    for i in range(0, len(ipconfig_result_list)): #逐行查找
        if  re.search(r'IPv4 地址' , ipconfig_result_list[i] ) != None:
            match_ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ipconfig_result_list[i]).group(0)  #由正则表达式获取ip地址
            for j in range(3,7):
                if re.search(r"适配器" , ipconfig_result_list[i - j] ) != None:
                    match_ip_dict[ipconfig_result_list[i - j]] = match_ip
    return match_ip_dict

if __name__ == '__main__':   #主程序入口
    ip_dict = get_ipconfig_ip() #返回字典ip_dict保存ip地址信息
    for i in ip_dict:
        print('{} {}'.format(i[0:-1], ip_dict[i])) #字符串format函数，其中i[0:-1]除去键的最后'\n'



