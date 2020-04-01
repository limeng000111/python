from selenium import webdriver
import time

chrome = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(chrome)
driver.implicitly_wait(10)
#open the url
#http://www.weather.com.cn/html/province/zhejiang.shtml
driver.get('http://www.weather.com.cn/html/province/zhejiang.shtml')
#find city
#please attention the infomation,city+(max+min)tmp
ele = driver.find_element_by_id('forecastID')
# print(ele.text)
ele01 = ele.text.split(u'℃\n')
# print(ele01)
for i in ele01:
    one = i.replace('℃','')
    # print(one)
    two = one.split('\n')
    # print(two)
    three = two[1].split('/')
    # print('three',three)
    curcity = [two[0]]
    # print('zhuge',curcity)
    low = three[1]

lowest = 40
low = int(low)
if low < lowest:
    lowest = low
    curcity = curcity
    print('最冷的城市：',curcity,'最低的温度:',lowest)
driver.quit()




# min = 40
# for caocao in liubei:
#     print("002",caocao)
    # mintemp = int(caocao[2])
    # if mintemp < 40:
    #     min = mintemp
    #     lowestcity = caocao[0]
    #     print(lowestcity)




