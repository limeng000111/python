#!/usr/bin/python
# -*- coding:UTF-8 -*-
#author:limeng    2019-6-22

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
 '''

#直接读取文本进行解析


html = etree.parse('c:\\Users\\dell\\Desktop\\xpath.html', etree.HTMLParser())
# result = etree.tostring(html)
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')#获取父节点
result = html.xpath('//li[@class="item-0"]/a/text()')#使用xpath中的text()方法获取节点中的文本
print(result)
print(type(result))
# html = etree.HTML(text)
# result = etree.tostring(html)
# result = html.xpath('//*')
# print(result.decode('UTF-8'))