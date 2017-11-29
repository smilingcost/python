# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

# 第三方 SMTP 服务
mail_host="smtp.ym.163.com"  #设置服务器
mail_user="zhangjingui@kabala365.com"    #用户名
mail_pass="Zjg123"   #口令


sender = 'zhangjingui@kabala365.com'
receivers = ['954950195@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("张进桂", 'utf-8')
message['To'] =  Header("954950195@qq.com", 'utf-8')
subject = '邮件测试'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
mail_msg="""
<p>邮件测试的</p>
<table border="2" bgcolor="#F0F8FF">
  <tr>
    <td>思沛</td>
    <td style="color:blue">公司</td>
    <td>下载</td>
   </tr></table>
<FONT color="#f00000"><a  href="http://www.baidu.com">百度</a>网站</FONT>
<p><img src="cid:image1"></p>
"""   #url必须加http ，邮件的 HTML 文本中一般邮件服务商添加外链是无效的
message.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('20171129100728.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.xlsx', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.xlsx"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string()) #Python SMTP 对象使用 sendmail 方法发送邮件
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"




