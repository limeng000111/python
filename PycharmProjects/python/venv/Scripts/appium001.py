from appium import webdriver
import time,traceback

#连接手机的属性
desired_caps ={
    'platformName':'Android',
    'platformVersion':'9',
    'device':'limeng',
    'appPackage':'com.zjiec.sellingworld',
    'appActivity':'com.zjiec.sellingworld.ui.SplashActivity',
    'noset':'True',
    'NewCommandTimeout':6000,
    'deviceName':'66J0218C03005237',


}

#连接Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

driver.find_element_by_id('com.ibox.calculators:id/digit7').click()

driver.find_element_by_id('com.ibox.calculators:id/mul').click()

driver.find_element_by_id('com.ibox.calculators:id/digit6').click()

driver.find_element_by_id('com.ibox.calculators:id/equal').click()

driver.find_element_by_id().click()