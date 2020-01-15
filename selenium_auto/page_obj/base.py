#-*-coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Page():
    base_url = 'https://www.demobizpal.com/partner/home'
    selenium_driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#页面基础类，用户所有页面进行继承
    def __init__(self,selenium_driver,base_url = base_url,parent = None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.parent = parent
        self.timeout = 30

    def _open(self):
        url = self.base_url
        self.driver.get(url)
        assert self.on_page(),'Did not land on%s'%url

    def on_page(self):
        return self.driver.current_url.encode('ntf-8') == (self.base_url + self.url)

    def open(self):
        self._open()

#查找单个元素
    def find_element(self,*loc):
        try:
            #加入显示等待
            # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print('未找到%s元素'%loc)

#查找多个元素
    def find_elements(self,*loc):
        return self.driver.find_element(loc)

    #输入参数
    def send_keys(self,loc,value,click_first=True,clear_first = True):
        try:
            if clear_first:
                self.driver.find_element(loc).clear()
            if click_first:
                self.driver.find_element(loc).click()
            self.driver.find_element(loc).send_keys(value)
        except ArithmeticError:
            print('没有找到元素%s'%loc)

