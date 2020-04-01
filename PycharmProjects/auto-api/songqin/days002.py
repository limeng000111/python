import time
from selenium import webdriver

#open chrome
chrome = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome)
driver.implicitly_wait(10)

#open the target url
driver.get('https://www.51job.com/')
ele = driver.find_element_by_id('kwdselectid')
ele.clear()
ele.send_keys('python')
res = driver.find_element_by_css_selector('body > div.content > div > div.fltr.radius_5 > div > button').click()
info = driver.find_elements_by_css_selector('#resultList div[class=el]')
print(info)






# driver.quit()