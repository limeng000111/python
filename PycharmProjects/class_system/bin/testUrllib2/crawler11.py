#!/usr/bin/limeng
#-*- coding:UTF-8 -*-
import time
import urllib.request
import os
import platform
import sys
import urllib.parse

def clear():
    print('加载2s，防止内容过多')
    time.sleep(5)
    OS = platform.system()
    if (OS == u"windows"):
        os.system('cls')
    else:
        os.system('clear')


def linkbaidu():
    url = 'https://testerhome.com/topics/'
    try:
        response = urllib.request.urlopen(url,timeout=5)
    except urllib.request.URLError:
        print(u"网络地址错误")
        exit()
    with open('c:\\Users\\dell\\Desktop\\baidu.txt',"wb") as fp:
        fp.write(response.read())
    print(u"url信息,response.geturl():%s"%response.geturl())
    print(u"url代码，response.getcode(): %s"%response.getcode())
    print(u"url具体信息，response.info():%s"%response.info())

if __name__ == "__main__":
    linkbaidu()
import re


respose= urllib.request.urlopen('http://www.xiaohuar.com/v/')
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容
urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
url=urls[5]
result=urllib.request.get(url)
mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

video=urllib.request.get(mp4_url)

with open('c:\\Users\\dell\\Desktop\\baidu.txt','wb') as f:
    f.write(video.content)

import hashlib
m = hashlib.md5
src = 'i like python'
m.update(src.encode('utf-8'))
print(m.hexdigest())




