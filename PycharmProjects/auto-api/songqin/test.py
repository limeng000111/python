#!/usr/bin/python
# -*-coding:UTF-8 -*-

import cgi,cgitb

#创建FiledStorage实例化
form = cgi.FieldStorage()

#获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("html")
print("head")
print("<meta charset = \"utf-8\">")
print("<title>test实例</title>")
print("head")
print("body")
print("<h2>%s官网：%s</h2>"%(site_name,site_url))
print("body")
print("html")