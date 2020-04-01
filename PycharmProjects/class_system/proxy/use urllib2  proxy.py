#/usr/bin/python
# -*- coding:UTF-8 -*-
# author:limeng  2019-6-22

import urllib
import sys
import re

def testArgument():
    '''测试输入一个参数，只需要输入一个参数'''
    if len(sys.argv) != 2:
        print(u"只需要一个参数就行了")
        tipUse()

        exit()
    else:
        TP = TestProxy(sys.argv[1])

def tipUse():
    '''显示提示信息'''
    print(u"该程序只能输入一个参数，这个参数必须是可用的proxy")
    print(u"usage: python testuellib2WithProxy.py  http://1.2.3.4.5")
    print(u"usags. python testUrllib2WithProxy.py  https://1.2.3.4.5")

class TestProxy():
    '''这个类的作用是测试proxy是否有效'''
    def __init__(self,proxy):
        self.proxy = proxy
        self.checkProxyFormat(self.proxy)
        self.url = 'http://www.baidu.com'
        self.timeout = 5
        self.flagword = "baidu"   #在网页返回数据中查找这个词
        self.useProxy(self.proxy)

    def checkProxyFormat(self,proxy):
        try:
            proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\:[\d]{1,5}$')
            re.search(proxyMatch,proxy).group()
        except AttributeError:
            tipUse()
            exit()
        flag = 1
        proxy = proxy.replace('//','')
        try:
            protocol = proxy.split(':')[0]
            ip = proxy.split(':')[1]
            port = proxy.split(':')[2]
        except IndexError:
            print("下标出界")
            tipUse()
            exit()
        flag = flag and len(proxy.split(':')) == 3 and len(proxy.split('.') ==4)

        flag = ip.split('.')[0] in map(str, range(1, 256))and flag
        flag = ip.split('.')[1] in map(str, range(1, 256))and flag
        flag = ip.split('.')[2] in map(str, range(1, 256))and flag
        flag = ip.split('.')[3] in map(str, range(1, 255))and flag

        '''这里实在检查proxy的格式'''
        if flag:
            print(u"输入的代理服务器符合标准")
        else:
            tipUse()
            exit()

    def useProxy(self,proxy):
        '''利用代理访问百度，并查找关键词'''
        protocol = proxy.split('//')[0].split(":",'')
        ip = proxy.split('//')[1]
        opener = urllib.build_opener(urllib.ProxyHandler({protocol:ip}))
        urllib.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.url,timeout = self.timeout)
        except:
            print(u'连接错误，退出程序')
            exit()
        str = response.read()
        if re.search(self.flagword,str):
            print(u"已取得关键词，该代理可用")
        else:
            print("该代理不可用")
if  __name__=="__main__":

    testArgument()



