import unittest
import time
from selenium import webdriver
import HTMLTestRunner

class test_develop(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.bizpalglobal.com/login?lang=zh-cn'
        chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome)
        self.driver.set_window_size(800,1000)
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

    def login(self,account,password):
        #输入邮箱账号
        self.driver.find_element_by_xpath('//*[@id="large-header"]/div[2]/div/div/div/ul/li[1]').click()
        box = self.driver.find_element_by_xpath('//*[@id="large-header"]/div[2]/div/div/div/div/div[1]/form/div[1]/input')
        box.click()
        box.send_keys(account)
        #输入邮箱密码
        self.driver.find_element_by_xpath('//*[@id="large-header"]/div[2]/div/div/div/div/div[1]/form/div[2]/div[1]').click()
        box_01 = self.driver.find_element_by_xpath('//*[@id="large-header"]/div[2]/div/div/div/div/div[1]/form/div[3]/input')
        box_01.click()
        box_01.send_keys(password)
        #点击登录
        self.driver.find_element_by_xpath('//*[@id="large-header"]/div[2]/div/div/div/div/div[1]/form/div[5]/button').click()
        #self.driver.implicitly_wait(10)
     #输入正确的账号密码
    def test_right(self):
        self.login('2421712196@qq.com','123456')

        #获取弹窗内容
        tip=self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div').text
        #//*[@id="layui-layer2"]/div/text()
        res = '登录成功'

        self.assertEqual(tip,res)

    def tearDown(self) :

        self.driver.quit()


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    file = 'C:/Users/dell/PycharmProjects/auto-api/report/' + now + '_testresult.html'
    fp = open(file, 'wb')  # 创建测试报告文件

    suite = unittest.TestSuite()  # 创建测试套件
    suite.addTest(test_develop('test_right'))  # 向测试套件中添加测试用例

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下：')
    runner.run(suite)  # 执行测试
    fp.close()
