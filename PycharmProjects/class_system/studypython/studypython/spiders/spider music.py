#-*- coding:UTF-8 -*-

import time
from selenium import webdriver
import re
import urllib.request
from lxml import etree

# #找到谷歌浏览器路径，并打开
# chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chrome_driver)
#
# #设置浏览器屏幕最大化
# driver.set_window_size(800,400)
#
# #设置隐式等待--10s
# driver.implicitly_wait(3)
#
# #打开网易云官网
# driver.get('https://music.163.com/')
#
# #防止网速加载过慢，停留2s
# time.sleep(2)
#
# driver.find_element_by_css_selector('#g_nav2 > div > ul > li:nth-child(2) > a').click()
#
# #获取歌曲名称
# music = re.compile('<b title="（.*?）">',re.S)
# print(type(music))
# print(music)

#请求头
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

#请求的url
url = 'https://music.163.com/#/discover/toplist'
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read()
result = etree.HTML(html)
result1 = etree.tostring(result)
print(html)



