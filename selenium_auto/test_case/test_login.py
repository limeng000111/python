import unittest
from page_obj.loginPage import login
from model.driver import browser
from page_obj.base import Page
from model import screenshot
from selenium import webdriver

class loginTest(unittest.TestCase):
    def login_verify(self,username='',passwd=''):
        d = browser()
        login(Page).login_oper(username,passwd)

    #输入正确的账号密码
    def test_sucess(self,username = '15055228674',passwd = '123456'):
        self.login_verify(username,passwd)
        self.assertEqual(login(Page).login_success_info(),'登陆成功')
        driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        screenshot.get_screenshot(driver)



if __name__ == '__main__':
    unittest.main()




