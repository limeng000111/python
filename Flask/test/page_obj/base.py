# #-*-coding:utf-8
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class Page(object):
#     base_url = 'https://www.demobizpal.com/partner/home'
#     selenium_driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# #页面基础类，用户所有页面进行继承
#     def __init__(self,selenium_driver,base_url = base_url,parent = None):
#         self.base_url = base_url
#         self.driver = selenium_driver
#         self.parent = parent
#         self.timeout = 30
#
# def _open(self):
#     url = self.base_url
#     self.driver.get(url)
#     # assert self.on_page(),'Did not land on%s'%url
#
# def on_page(self):
#     return self.driver.current_url.encode('ntf-8') == (self.base_url + self.url)
#
# def open(self):
#     self._open()
#
# #查找单个元素
# def find_element(self,*loc):
#     try:
#             #加入显示等待
#             # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
#         WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
#         return self.driver.find_element(*loc)
#     except:
#         print('未找到%s元素'%loc)
#
# #查找多个元素
# def find_elements(self,*loc):
#     return self.driver.find_element(loc)
#
#     #输入参数
# def send_keys(self,loc,value,click_first=True,clear_first = True):
#     try:
#         if clear_first:
#             self.driver.find_element(loc).clear()
#         if click_first:
#             self.driver.find_element(loc).click()
#         self.driver.find_element(loc).send_keys(value)
#     except ArithmeticError:
#         print('没有找到元素%s'%loc)
#
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


class Page(object):



    base_url = "https://www.demobizpal.com/partner/login"

    def __init__(self, selenium_driver, base_url=base_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self):
        url = self.base_url
        self.driver.get(url)
        # assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open()

    def on_page(self):
        #return (self.driver.current_url).encode('utf-8') == (self.base_url + self.url)
        return self.driver.current_url.encode('utf-8') == (self.base_url + self.url)

def find_element(self, *loc):
    # return self.driver.find_element(*loc)
    try:
    # 确保所有元素是可见的
    # 注意：以下入参为元组的元素，需要加*。python存在这种特性，就是将入参放在元组里。
    #WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
    # 注意：以下入参本身是元组，不需要加*
        print('-------------------------------------')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)
    except:
        print("%s 页面中未能找到%s元素"%(self, *loc))

def find_elements(self, *loc):
    return self.driver.find_elements(*loc)

def script(self, src):
    return self.driver.execute_script(src)

def swtich_frame(self, loc):
    return self.driver.swith_to_frame(loc)

def send_keys(self, loc, value, clear_first=True, click_first=True):
    try:
    # getattr相当于self.loc
        loc = getattr(self, "_%s" % loc)
        if click_first:
            self.find_element(*loc).click()
        if clear_first:
            self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(value)
    except ArithmeticError:
        print ("%s 页面中未能找到 %s 元素" % (self, loc))