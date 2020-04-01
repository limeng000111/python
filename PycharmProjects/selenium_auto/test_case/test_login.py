# import unittest
# from page_obj.loginPage import login
# from model.driver import browser
# from page_obj.base import Page
# from model import screenshot
# from selenium import webdriver
# from model.setup import MyTest
# from model.setup import MyTest
# import time
#
# class loginTest(MyTest):
#     def login_verify(self,username='',passwd=''):
#         # time.sleep(10)
#         login(self.driver).login_oper(username,passwd)
#
#     #输入正确的账号密码,username = '15055228674',passwd = '123456'
#     def test_sucess(self):
#         self.login_verify(username = '15055228674',passwd = '123456')
#         time.sleep(3)
#         po = login(self.driver)
#         self.assertEqual(po.login_success_info(),'登陆成功')
#
#         # self.assertEqual(po.login_success_info(),'登陆成功')
#         # driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#         # screenshot.get_screenshot(driver)
#
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#

from time import sleep
import unittest, random, sys
from model import setup
from page_obj.loginPage import login
from model.screenshot import get_screenshot
import time
from model import HTMLTestRunner


class loginTest(setup.MyTest):

    '''
    测试用户登录
    '''

    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login_right(self):
    #'''用户名、密码正确'''
        self.user_login_verify(username="15055228674" , password="123456")
        get_screenshot(self.driver)
        # sleep(1)
        po = login(self.driver)
        self.assertEqual(po.login_user_success(), '登录成功')
        # get_screenshot(self.driver)


    def test_login_miss_user(self):
        #不输入账号--直接输入密码
        self.user_login_verify(username='',password='123456')
        get_screenshot(self.driver)
        sleep(1)
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(),'请填写正确的邮箱或者手机号！')
        # get_screenshot(self.driver)

    def test_login_miss_passwd(self):
        #输入账号不输入密码
        self.user_login_verify(username='15055228674',password='')
        get_screenshot(self.driver)
        sleep(1)
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(),'请填写密码！')

    def test_login_dubbo_miss(self):
        #账号密码都为空
        self.user_login_verify(username='',password='')
        get_screenshot(self.driver)
        sleep(1)
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(),'请填写正确的邮箱或者手机号！')





if __name__ == '__main__':
    unittest.main()
    # # file_path ='C:\\Users\\dell\\PycharmProjects\\selenium_auto\\report\\' + time.strftime('%Y-%m-%d%H_%M_%S',time.localtime(time.time())) +'.html'
    # file_path = r'C:\Users\dell\PycharmProjects\selenium_auto\report\bizpal.html'
    # #指定批量执行的模块
    # test_module = './'
    # discover = unittest.defaultTestLoader.discover(test_module,pattern='test*.py')
    # #打开文件，写入测试结果
    # with open(file_path,'w+') as f:
    #     runner = HTMLTestRunner(stream = f,verbosity=2,title='畅销天下测试报告',description='用例执行详情' )
    #     runner.run(discover)
    # f.close()
    #
