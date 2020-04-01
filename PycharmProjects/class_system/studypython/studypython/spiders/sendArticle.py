#-*-coding:UTF-8 -*-
from selenium import webdriver
import time
import datetime
import random
from selenium.webdriver.common.keys import Keys
#设置浏览器


chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
# time.sleep(5)
#运行chrome,打开浏览器
# driver = webdriver.Chrome()
#设置浏览器窗口（最大化）
driver.maximize_window()

#设置全局操作时间
driver.implicitly_wait(5)

#打开网址
driver.get("http://service.democnsellers.cn/#/login?redirect=%2Fdashboard")

#睡5秒
time.sleep(2)
#选择账号登录
driver.find_element_by_css_selector("#app > div > div.login-right > form > div:nth-child(4) > div > div > input").click()
#点击输入用户姓名框，清空数据
# driver.find_element_by_xpath('//*[@id="J-userName"]').click()
#输入手机号和密码
# driver.refresh()
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys('111222@qq.com')
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys('123456')
#点击登录
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[5]/div/button').click()
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[5]/div/button').click()
#校验是否登陆成功
#
# Code = ''
# while Code != 200:
#     print('登陆失败，重新登陆')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[5]/div/button').click()
# str = driver.find_element_by_css_selector('body > div.el-message.el-message--error > i').text
# if str == '连接超时':
#   driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[5]/div/button').click()
# else:
#   pass


#刷新页面
# driver.refresh()
#进入页面，点击：新建动态：
time.sleep(2)
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.dashboard-draft > div.draft-title > button > span').click()
#选中标题
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-top > div:nth-child(2) > div.editor-title > textarea').click()
#输入标题
nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");#生成当前时间
randomNum=random.randint(0,100);#生成的随机整数n，其中0<=n<=100
if randomNum<=10:
  randomNum=str(0)+str(randomNum);
uniqueNum=str(nowTime)+str(randomNum);

driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-top > div:nth-child(2) > div.editor-title > textarea').send_keys('自动化发布服务商文章00%s'% uniqueNum )
#输入文章作者
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-top > div:nth-child(2) > div.editor-author > input[type="text"]').send_keys('测试')
#输入文章内容
driver.find_element_by_xpath('//*[@contenteditable="true"]').send_keys('自动化设置服务商文章')
#点击上传图片按钮
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div.upload-btn > div > div > button').click()
#上传本地图片
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div.upload-btn > div > div > input').send_keys('C:\\Users\\dell\\Desktop\\a4ce53aad25ba0576dd0be35826a3d0d.jpg')
#跳进选择图片页面
# driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div:nth-child(3) > div > div > div.el-dialog__body > div')
#选择2.35:1图片
time.sleep(2)
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div:nth-child(3) > div > div > div.el-dialog__body > div > div.cropper-wrap > div:nth-child(4) > div > div > button:nth-child(1)').click()
time.sleep(2)
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div:nth-child(3) > div > div > div.el-dialog__body > div > div.cropper-wrap > div:nth-child(4) > button').click()
time.sleep(2)
#选择1:1图片
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div:nth-child(3) > div > div > div.el-dialog__body > div > div.cropper-wrap > div:nth-child(4) > div > div > button:nth-child(2)').click()
time.sleep(2)
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div:nth-child(3) > div > div > div.el-dialog__body > div > div.cropper-wrap > div:nth-child(4) > button').click()
time.sleep(2)
#点击完成
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.content > div.content-right > div.right-bottom > div.upload-picture > div:nth-child(3) > div > div > div.el-dialog__footer > span > button.el-button.el-button--primary').click()
time.sleep(2)
print('ok')
# #向上滑动鼠标
# js="var q=document.documentElement.scrollTop=0"
#
# driver.execut_script(js)
#点击“发送审核”
driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.header > div:nth-child(2) > button:nth-child(3)').click()
time.sleep(2)
print('it is over')
# driver.switch_to_window(driver.window_handles[0])

#退出
driver.quit()