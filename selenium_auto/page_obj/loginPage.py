from selenium.webdriver.common.by import By
import time
from page_obj.base import Page

class login(Page):
    url = '/'
    #获取登录姓名
    login_username_loc = (By.XPATH,'//*[@id="user"]')
    #获取登录密码
    login_passwd_loc = (By.ID,'pwd')
    #获取登录按钮
    login_button_loc = (By.ID,'submit')
    #获取登陆时的错误提示
    login_error_loc = (By.XPATH,'/html/body/div[2]/p')
    #获取登陆时的正确提示
    login_sucess_loc = (By.XPATH,'//body/div[2]/p')

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_passwd(self,passwd):
        self.find_element(*self.login_passwd_loc).clear()
        self.find_element(*self.login_passwd_loc).send_keys(passwd)

    #点击登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).clear()

    #登录操作
    def login_oper(self,username,passwd):
        self.login_username(username)
        self.login_passwd(passwd)
        self.login_button()
        time.sleep(5)

    #获取登录错误信息
    def login_error_info(self):
        return self.find_element(*self.login_error_loc).text

    #获取登录成功返回的信息
    def login_success_info(self):
        return self.find_element(*self.login_sucess_loc).text

