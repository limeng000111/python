#-*-coding:UTF-8-*-
import  requests
import time
import json
import pytest
import allure
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# @pytest.fixture(scope='moudle')

def test_get_info():
    data = {"request_type":"android","page":"0","lang":"zh-cn","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1Njg4NjM5ODksImV4cCI6MTU2OTQ2ODc4OSwidXNlcl9pZCI6IjE1NTgwNTk1NTYiLCJzaG9wX2lkIjoiMCJ9.RElozf6q9wqqhIoC0IqGe4DXlWQKlbrbTTUOBPo9oRU"}
    url = "http://api.demobizpal.com/v_2_0_0/News/getNewslist"
    # headers={"Content-Type":"application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; HMA-AL00 Build/HUAWEIHMA-AL00)","Connection": "Keep-Alive"}


    req = requests.post(url=url,data=data)
    print(req.status_code)
    # print(req.json())
    news = req.json()["data"]
    # print(news_id)
    count = news.count("news_id")
    # print("count",count)
    new_len=[]
    for new in news:
        # print(new["news_id"])
        # print(new['titles'])
        print("{} : {}".format(new["news_id"],new["titles"]))
        new_len.append(new)
    res = len(new_len)
    print("此页新闻的条数：",res)
    assert res == 10


#发送邮件
def send_email():
    sender = '2421712196@qq.com'
    receiver = 'limeng@cnsellers.com'
    smtpserver = 'smtp.163.com'
    username = '2421712196@qq.com'
    password = 'limeng7852889'

    # 邮件主题
    mail_title = '畅销天下测试报告'

    # 读取html文件内容
    f = open(r'C:\Users\dell\PycharmProjects\python\venv\Scripts\report.html', 'rb')
    mail_body = f.read()
    f.close()

    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("发送邮件失败！！！")

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    test_get_info()
    send_email()



# get_info()
