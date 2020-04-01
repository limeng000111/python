import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import configparser as cparser
import time

class sendEmail():
    time.sleep(1)
    #发送邮件服务器
    smtpserver = 'smtp.qq.com'

    #发送邮箱用户名和密码
    user = '2421712196@qq.com'
    password = 'limeng7852889'
    mail_pass = 'pzmoihttlmlpecbe'

    #发送和接收邮箱
    sender = '2421712196@qq.com'
    recevicer = '2421712196@qq.com'

    #发送邮件主题和内容
    subject = 'app接口自动化测试结果'

    #获取最新的报告（配置文件）
    def get_dir():
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\','/')
        file_path = base_dir + '/mysql/db_config.ini'

        # print(file_path)
        # logger.INFO(file_path)

        #初始化获取配置信息的实例
        cf = cparser.ConfigParser()
        cf.read(file_path)
        #测试报告的路径
        test_dir = cf.get('file','test_dir')
        return test_dir

    test_dir = get_dir()

    def new_file(test_dir):
        #列举test_dir目录下的所有文件，结果以列表形式返回
        lists = os.listdir(test_dir)
        #根据修改时间从小到大排序
        lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
        # 获取最新文件的绝对路径
        file_path = os.path.join(test_dir, lists[-1])
        return file_path
    #最新的测试报告
    newest_report = new_file(test_dir)
    #邮件正文
    f = open(newest_report,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['subject'] = Header(subject,'utf-8')
    msg['from'] = sender
    msg['To'] = recevicer

    #SSL协议端口使用465
    smtp = smtplib.SMTP_SSL(smtpserver,465)

    #向用户标识用户身份
    smtp.helo(smtpserver)
    #服务器返回结果确认
    smtp.ehlo(smtpserver)
    #登录
    smtp.login(user,mail_pass)

    print('start send email')

    smtp.sendmail(sender,recevicer,msg.as_string())
    smtp.quit()
    print('send email end')

send_email = sendEmail()

