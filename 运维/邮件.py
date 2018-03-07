# coding=utf-8
import smtplib
import string

HOST = "smtp.ym.163.com"         
SUBJECT = "Test email from Python"      # 定义邮件主题
TO = "zhangjingui@gzsipei.net"       #定义邮件收件人
FROM = "zhangjingui@kabala365.com"   #定义邮件发件人
text = "Python rules them all!"     # 邮件内容
BODY = string.join((          # 组装 sendma il 方法的邮件主体内容 ，各段以 ” ＼r \ n ” 进行分隔 ” From : % s”
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP()      #创建一个 SMTP （ ） 对象
server.connect(HOST,"25")   # 通过 connect 方法连接 smtp 主机
server.starttls()        # 启动安全传输模式
server.login("zhangjingui@kabala365.com","***")      # 邮箱账号登录校验
server.sendmail(FROM, [TO], BODY)            # 邮件发送
server.quit()  # 断开 smtp 连接




