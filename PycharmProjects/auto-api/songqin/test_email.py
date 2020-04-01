import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
import logging
#发件人邮箱
my_sender = '2421712196@qq.com'
#发件人邮箱密码
my_passwd = 'igvlmkbcqeljebbc'
#收件人邮箱
my_user = 'limeng@cnsellers.com'
logging.basicConfig(level=logging.INFO,format='%(asctime)s    %(levelname)s: %(message)s')
def mail():
    ret = True
    try:
        massage = MIMEText('hello, it is my first email','plain','utf-8')
        massage['From']=formataddr(["guomaoyunshang",my_sender])#发送邮箱账号
        massage['to']=formataddr(['畅销天下',my_user])#接收邮箱账号
        massage['subject']='test,test'   #邮件的主题

        server = smtplib.SMTP_SSL('smtp.qq.com',465)#启用SMTP服务器，端口号25
        server.login(my_sender,my_passwd)#使用账号密码登录
        logging.info('连接SMTP成功')
        server.sendmail(my_sender,[my_user,],massage.as_string())#发送邮件，转换成string类型

        server.quit()
    except Exception:
        ret = False
    return ret
ret = mail()
if ret:
    print('邮件发送成功')
else:
    print('邮件发送失败')


