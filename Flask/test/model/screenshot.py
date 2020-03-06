#封装截图操作
from selenium import webdriver
import os,sys
import time
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
def get_screenshot(driver):
    current_time = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
    # base_dir = os.path.split(__file__)[0]#获取的的元祖
    # base_dir = str(base_dir)
    # print(base_dir)
    # base_dir = base_dir.replace('\\','/')
    # image = base_dir + current_time +'.png'
    # print(image)
    # driver.get_screenshot_as_file
    try:
        base_dir = 'C:\\Users\\dell\\PycharmProjects\\Flask\\test\\picture\\' + current_time +'.png'
        driver.get_screenshot_as_file(base_dir)
        print('截图成功，请在文件夹下查看')
    except BaseException as msg:
        print(msg)


if __name__ == '__main__':
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get('https://www.demobizpal.com/partner/home')
    get_screenshot(driver)
    driver.quit()