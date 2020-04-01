#time:2019-11-18
#-*-coding:utf-8-*-
import unittest
import json
import requests
import logging
import time
import random
from test_api import HTMLTestRunner
class login(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://api.demobizpal.com/v_2_0_0/user_manage/verifiCodeLogin'
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')

    #快捷登录
    def test_mobile(self):
        url = self.url
        data = {"mobile":18856213800,"login_type":12,"device_id":"141fe1da9ec27f92f83",
            "code":363636,"lang":"zh_cn","request_type":"ios","countrycode":86}
        res = requests.post(url=url,data=data)
        result = res.json()
        self.assertEqual(result['status'],200)
        # logging.info(res.json())
    #环境为预发布（url）
    def test_fail_url(self):
        url_right = 'http://api.demobizpal.com/v_2_0_0/user_manage/verifiCodeLogin'
        url = 'http://api.prebizpal.com/v_2_0_0/user_manage/verifiCodeLogin'
        data = {"mobile": 18856213800, "login_type": 12, "device_id": "141fe1da9ec27f92f83",
                "code": 363636, "lang": "zh_cn", "request_type": "ios", "countrycode": 86}
        res = requests.post(url=url, data=data)
        result = res.json()
        # logging.info(res.json())
        try:
            self.assertEqual(result['status'],200)
            self.assertEqual(url,res.url)
            self.assertEqual(result['data']['user_truename'],'国贸云商')

        except Exception as e:
            print('请求的url: ',url)
            print('请求的参数: ',data)
            raise e
    #错误的验证码(363637)
    def test_fail_code(self):
        url = 'http://api.prebizpal.com/v_2_0_0/user_manage/verifiCodeLogin'
        data = {"mobile": 18856213800, "login_type": 12, "device_id": "141fe1da9ec27f92f83",
                "code": 363637, "lang": "zh_cn", "request_type": "ios", "countrycode": 86}
        res = requests.post(url=url, data=data)
        result = res.json()
        # logging.info(result)
        self.assertEqual(result['msg'],'验证码不正确')
        # self.assertEqual()

    #随机生成手机号进行注册
    def test_register(self):
        mobile_head = ['130','131','132','133','151','152','153','155','156']
        mobile = random.choice(mobile_head)+''.join(random.choice('0123456789') for i in range(8))
        logging.info(mobile)
        url = self.url
        data = {"mobile": mobile, "login_type": 12, "device_id": "141fe1da9ec27f92f83",
                "code": 363636, "lang": "zh_cn", "request_type": "ios", "countrycode": 86}
        res = requests.post(url=url, data=data)
        result = res.json()
        # logging.info(result)
        self.assertIsNotNone(result['data']['token'])



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(login('test_mobile'))
    suite.addTest(login('test_fail_url'))
    suite.addTest(login('test_fail_code'))
    suite.addTest(login('test_register'))
    # with open (r'.\result','wb')  as f:
    fp = open('c:\\Users\\dell\\PycharmProjects\\Bizpal\\test_report\\result.html','wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = 'html测试报告',description = 'unittest测试报告',verbosity = 2)
    print('-------------------------------------')
    runner.run(suite)




