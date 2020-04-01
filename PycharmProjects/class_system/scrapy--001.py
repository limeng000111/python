#!/usr/bin/python
#-*-coding:UTF-8 -*-

from scrapy.selector import Selector
with open('c:\\Users\\dell\\Desktop\\aaa.xml','r')  as fp:
    body = fp.read()
    body1 = Selector(text=body).xpath('//a[1][@Name: My image 5]').extract()
    print(body)
    print(body1)
