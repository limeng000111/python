#-*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText

# Settings of sender's server
host = 'smtp.qq.com'
sender = '2421712196@qq.com'
user = '2421712196@qq.com'
password = input('请输入您的密码')
to = ['1362992685@qq.com']

# Content of email
subject = 'Python send html email test(简化版)'
with open(r'C:\Users\dell\Desktop\ooo.txt', 'rb') as f:
    content = f.read()

# Settings of the email string
email = MIMEText(content,'html','utf-8')
email['Subject'] = subject
email['From'] = sender
email['To'] = to[0]
msg = email.as_string()

# Login the sender's server
print('Logging with server...')
smtpObj = smtplib.SMTP()
smtpObj.connect(host, 25)
smtpObj.login(user, password)
print('Login successful.')

# Send email
smtpObj.sendmail(sender, to, msg)
smtpObj.quit()
print('Email has been sent')
