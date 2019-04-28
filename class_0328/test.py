import smtplib
import ssl
from conf import emailname, emailpwd

server = smtplib.SMTP('smtp.163.com', 25)
emailname = '13871180488@163.com'
emailpwd = 'zpj19880913'


server.login(emailname, emailpwd)
server.sendmail(emailname, '542126547@qq.com', 'hello')
server.quit()


