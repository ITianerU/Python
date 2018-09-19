import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>

        <h1> 这是一封来自python的html格式邮件</h1>
        <h6> 这是一封来自python的html格式邮件2</h6>

        </body>
        </html>
        """
#MIMEText创建一封邮件   html表示发送html格式的文件
msg = MIMEText(mail_content,"html","utf-8")
#发件人
msg["From"] = Header("小峰<xxxx@qq.com>","utf-8")
#收件人
msg["To"] = Header("小田<xxxx@qq.com>","utf-8")
#主题
msg["Subject"] = Header("pythonMailTest")

try:
    mailServer = smtplib.SMTP_SSL("smtp.qq.com".encode(),465)
    mailServer.login("发送邮箱账号", "邮箱授权码")
    mailServer.sendmail("发送邮箱账号", ["接收邮箱账号1", "接收邮箱账号2"], msg.as_string())
    mailServer.quit()
except Exception as e:
    print(e)