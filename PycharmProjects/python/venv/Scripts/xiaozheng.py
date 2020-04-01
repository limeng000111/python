#-*- coding:utf-8 -*-
import requests
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import re
# def weather():
#     # #启动driver
#     # chome = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#     # driver = webdriver.Chrome(chome)
#     #
#     # #设置屏幕：全屏,隐式等待10s
#     # driver.maximize_window()
#     # driver.implicitly_wait(10)
#     #
#     # #打开链接
#     # #手动找到url
#     header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#     url = 'http://www.weather.com.cn/weather/101210101.shtml'
#     # driver.get(url,header)
#     req = requests.get(url,header)
#     # weather=driver.find_element_by_xpath('//*[@id="7d"]/ul/li[1]/big[1]')
#     # print(req.content.decode("utf-8"))
#     html = req.content.decode("utf-8")
#     soup = BeautifulSoup(html,'lxml')
#     res = soup.find('div',id = '7d')
#     # print(res)
#     res = str(res)
#     # print(res)
#     pattern = re.compile('<span>(.*?)</span>/<i>(.*?)℃</i>',re.S)
#
#     items = re.findall(pattern,res)
#     # print(items)
#     #当天的最高温度和最低温度
#     mintem = items[0][1]
#     maxtem = items[0][0]
#     print("当天最高温度：",maxtem,"当天最低温度：",mintem)
#     #第二天的最高&&最低温度
#     next_mintem = items[1][1]
#     next_maxtem = items[1][0]
#     print("明天最高温度：",next_maxtem,"当天最低温度：",next_mintem)
#
#     #当天天气状况
#     patternone= re.compile('<p class="wea" title="多云转晴">(.*?)</p>',re.S)
#     itemsone= re.findall(patternone,res)
#     sky = itemsone[0]
#     print("当天的天气：",sky)
#
#     my_sun = "亲耐的郑小胖","当天最高温度：",maxtem,"当天最低温度：",mintem,"天气：",sky
#     "明天最高温度：", next_maxtem, "当天最低温度：", next_mintem
#     my_sun=str(my_sun)
#
#     # items = list(items)
#     # item = []
#     # for item in items:
#     #
#     #     print(item)
#
#     #将天气情况写入文本
# # def write(my_sun):
# #     """
# #     将天气状况写入doc
# #     :return:
# #     """
#
# #抓取暖心的话
#
#
#     with open(r"C:\Users\dell\Desktop\ooo.txt",'w',encoding='utf-8') as f:
#         f.write(my_sun)
#         print('写入成功')
#
# def words():
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#     url = 'https://www.duanwenxue.com/article/4614705.html'
#     res = requests.get(url,header)
#     html = res.content
#     soup = BeautifulSoup(html,'lxml')
#     words_warm = soup.find_all('p')
#     words_warm=str(words_warm)
#     print(words_warm)
#
# weather()
# words()
#     my_sun = "当天最高温度：", maxtem, "当天最低温度：", mintem, "天气：", sky
#     "明天最高温度：", next_maxtem, "当天最低温度：", next_mintem
#     write()

def get_words():
    """
    获取金山词霸的接口，每日更新
    :return:
    """
    req = requests.get('http://open.iciba.com/dsapi/')
    result = req.json()
    content_EN = result['content']
    contrnt_CN = result['note']
    date = result['dateline']

    return contrnt_CN,content_EN,date

def get_weather():
    """
    高德地图接口
    生成key：2b48ff304a19d4f3582da5e8a307003e
    获取城市code:330100
    :return:
    """
    code = '330100'
    key = 'f9859d86308f6ae49928735ec364c469'
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=%s&city=%s'.format(key,code)
    print(url)
    req = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?key={0}&city={1}'.format(key,code))
    # https: // restapi.amap.com / v3 / weather / weatherInfo?city =330100& key =2b48ff304a19d4f3582da5e8a307003e

    weather = req.json()
    if weather['status'] == '1':
        print('it is ok')
        return weather['lives']

    else:
        print("sorry,it is error:" + weather['info'])
        return None
    print(weather['forecasts'][0]['casts'][0])

    # word = [date,
    #         content_EN,
    #         contrnt_CN]
    # print(word)

def get_time():
    #获取时间
    return time.strftime("%Y-%m-%d %H:%M:S,time.localtime()")


def make_soup():
    """
    制作鸡汤
    :return:
    """
    soup = get_words()
    weather = get_weather()

    if weather is None:
        time.sleep(3)
        weather = get_weather()

    title = "早上好！"
    # desp =




# if __name__=='__main__':
    get_words()
    get_weather()



