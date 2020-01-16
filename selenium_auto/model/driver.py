from selenium import webdriver
from selenium.webdriver import Remote
import sys
import time
import configparser
#封装浏览器驱动
#创建配置文件对象
con = configparser.ConfigParser()
file = r'C:\Users\dell\PycharmProjects\selenium_auto\model\bizpal.ini'
#读取文件
con.read(file,encoding='utf-8')
def browser():
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    # driver.maximize_window()
    # driver.get('https://www.demobizpal.com/partner/home')
    # url = con.get('manager', 'url')
    # driver.get(url)
    # time.sleep(5)
    return driver
    # driver.get('https://www.demobizpal.com/partner/home')

if __name__ == '__main__':
    d = browser()
    d.get('https://www.demobizpal.com/partner/home')
    d.quit()

