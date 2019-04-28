import smtplib

from conf import emailname, emailpwd
#coding=utf-8
import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser

class SendMail():
    @classmethod
    def send_test_report(cls):
        cf = ConfigParser()
        cf.read("demo.cfg", encoding="utf-8")
        # sender = cf.get("sender","username")
        # receiver = cf.get("receiver","receiverName")

        sender = cf.get('email','sender')
        receiver = cf.get("email", "receiver")
        auth_code = cf.get("email", "auth_code")




        #邮件信息配置. 授权码 xdclass123
        # sender = '542126547@qq.com'
        # receiver = 'zpjpatrick@126.com'
        # auth_code = 'fanlneesrsplbdjf'  #设置客户端授权码，不是密码

        smtpserver = 'smtp.qq.com'
        subject = '自动化测试报告'


        #读取文件内容
        f = open("result.html", 'rb')
        mail_body = f.read()
        f.close()



        #HTML 形式的文件内容
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        html['Subject'] = subject
        html['from'] = sender
        html['to'] = receiver



        # html附件 将测试报告放在附件中发送
        att1 = MIMEText(mail_body, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="result.html"'  # 这里的filename可以任意写



        msg = MIMEMultipart()
        msg['Subject'] = subject  # 邮件的标题
        msg.attach(html)  # 将html附加在msg里
        msg.attach(att1)  # 新增一个附件



        #连接 登录 上smtp服务器
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login(sender, auth_code)

        #发送邮件
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

if __name__ == "__main__":
    SendMail = SendMail()
    SendMail.send_test_report()

