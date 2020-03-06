from test.model.driver import browser

import unittest
from selenium import webdriver
import time
#初始化浏览器的启动和关闭
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)#隐式等待10s，要学会使用显示等待
        self.driver.maximize_window()#窗口最大化
        #self.driver.set_window_size()  #设置窗口大小

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()