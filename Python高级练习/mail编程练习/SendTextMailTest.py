import smtplib
from email.mime.text import MIMEText

#MIMEText创建一封邮件   plain表示文本邮件
msg = MIMEText("这是一封来自python的邮件","plain","utf-8")

try:
    mailServer = smtplib.SMTP_SSL("smtp.qq.com".encode(),465)
    mailServer.login("发送邮箱账号","邮箱授权码")
    mailServer.sendmail("发送邮箱账号",["接收邮箱账号1","接收邮箱账号2"],msg.as_string())
    mailServer.quit()
except Exception as e:
    print(e)