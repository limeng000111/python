import unittest
from selenium import webdriver
import time
#
class MyTest(unittest.TestCase):

    # 每个测试用例执行前操作
    def setUp(self):
        chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        # time.sleep(5)
        # 运行chrome,打开浏览器
        # driver = webdriver.Chrome()
        # 设置浏览器窗口（最大化）
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')


    # @classmethod
    # #必须要使用@classmethod，所有的test运行完后运行一次
    # def tearDownClass(self):
    #     print('333')
    # @classmethod
    # def setUpClass(self):
    #     print('444')

    #测试用例
    def test_baidu_python(self):
        self.driver.find_element_by_id('kw').click()
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('python')
        #点击搜索
        self.driver.find_element_by_css_selector('#su').click()

        #匹配
        time.sleep(2)
        tag=self.driver.find_element_by_xpath('//*[@id="3"]/h3/a/em').text
        self.assertEqual('Python', tag)

        # 每个测试用例执行完后操作
        def tearDown ( self ):
            print('111')



if __name__ == '__main__':
    unittest.main(verbosity=2)#执行所有测试用例




