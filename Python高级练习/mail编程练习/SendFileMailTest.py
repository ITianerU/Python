import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart

#创建一封邮件实例,作为邮件容器容纳邮件信息和附件
mail = MIMEMultipart()

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

#将邮件内容装到容器中
mail.attach(msg)

#打开文件
with open("mail.txt","r",encoding="utf-8") as f:
    s = f.read()
    m = MIMEText(s,'base64','utf-8')
    m["Content-Type"] = "application/octet-stream"
    # 1. filename 后面需要用引号包裹，注意与外面引号错开
    m["Content-Disposition"] = "attachment; filename='mail.txt'"
    # 添加到MIMEMultipart
    mail.attach(m)

try:
    mailServer = smtplib.SMTP_SSL("smtp.qq.com".encode(),465)
    mailServer.login("发送邮箱账号", "邮箱授权码")
    mailServer.sendmail("发送邮箱账号", ["接收邮箱账号1", "接收邮箱账号2"], mail.as_string())
    mailServer.quit()
except Exception as e:
    print(e)