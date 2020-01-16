# from selenium.webdriver.common.by import By
# import time
# from page_obj.base import Page
# from page_obj.base import find_element
# from page_obj.base import _open
#
# class login(Page):
#     url = '/'
#     #获取登录姓名
#     login_username_loc = (By.ID,'user')
#     #获取登录密码
#     login_passwd_loc = (By.ID,'pwd')
#     #获取登录按钮
#     login_button_loc = (By.ID,'submit')
#     #获取登陆时的错误提示
#     login_error_loc = (By.XPATH,'/html/body/div[2]/p')
#     #获取登陆时的正确提示
#     login_sucess_loc = (By.XPATH,'//body/div[2]/p')
#
#     #登录用户名
#     def login_username(self,username):
#         find_element(*self.login_username_loc).clear()
#         find_element(*self.login_username_loc).send_keys(username)
#
#     #登录密码
#     def login_passwd(self,passwd):
#         find_element(*self.login_passwd_loc).clear()
#         find_element(*self.login_passwd_loc).send_keys(passwd)
#
#     #点击登录按钮
#     def login_button(self):
#         find_element(*self.login_button_loc).clear()
#
#     #登录操作
#     def login_oper(self,username,passwd):
#         _open(self)
#         self.login_username(username)
#         self.login_passwd(passwd)
#         self.login_button()
#         time.sleep(5)
#
#     #获取登录错误信息
#     def login_error_info(self):
#         return find_element(*self.login_error_loc).text
#
#     #获取登录成功返回的信息
#     def login_success_info(self):
#         return find_element(*self.login_sucess_loc).text

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_obj.base import Page
from time import sleep
from page_obj.base import *

class login(Page):

    '''
    用户登录界面
    '''
    url = '/'
    # 登录用户名的定位
    login_username_loc = (By.ID, 'user')

    #获取登录密码
    login_passwd_loc = (By.ID,'pwd')
    #获取登录按钮
    login_button_loc = (By.ID,'submit')
    #     #获取登陆时的错误提示
    login_error_loc = (By.XPATH,'/html/body/div[2]/p')
    #     #获取登陆时的正确提示
    login_sucess_loc = '//body/div[2]/p'

    # 登录用户名
    def login_username(self, username):
        # print(self.login_username_loc)
        self.driver.find_element_by_id('user').click()

        self.driver.find_element_by_id("user").send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.driver.find_element_by_id("pwd").clear()
        self.driver.find_element_by_id("pwd").send_keys(password)

    # 登录按钮
    def login_button(self):
        self.driver.find_element_by_id("submit").click()

    # 统一登录入口
    def user_login(self, username="", password=""):
    # 获取用户名和页面登录
        self._open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        # sleep(3)

    # 登录错误提示信息
    def login_error_hint(self):
        return  self.driver.find_element_by_xpath('/html/body/div[2]/p').text

    # 登录成功用户名信息
    def login_user_success(self):
        #return self.find_element(*self.login_user_success_loc).text
        username = self.driver.find_element_by_xpath('//body/div[2]/p').text
        return username

        # return username

