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
    # driver.get('https://www.demobizpal.com/partner/home')
    url = con.get('manager', 'url')
    driver.get(url)
    time.sleep(5)
    # return driver

# if __name__ == '__main__':
#     url = con.get('manager','url')
#     # print(url)
# d = browser()
# d.get(url)
    # time.sleep(3)
    # d.quit()

