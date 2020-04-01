#!/usr/bin/python
#-*-coding:UTF-8-*-
# def login(funct):
#     def inner(*args,**kwargs):
#         print('passed user veriftation')
#         return funct(*args,**kwargs)  ##inner的返回值
#     return inner
# #@login
# def tv(*args,**kwargs):
#     print('welcome %s to TV page %s ' % (args, kwargs))
#     return 88    #返回值
#
# tv = login(tv)
# dic = {'k1':'v1','k2':'v2'}
# l1 = ['python','java']
# t = tv(l1,dic)
# print(t)

#验证函数
# def login(*args,**kwargs):
#     print('%s登陆验证%s！'%(args,kwargs))
# #登陆后操作
# def quanxian(*args,**kwargs):
#     print('%s登陆后操作！%s'%(args,kwargs))
# #装饰器
# def decorator(login_func,quanxian_func): #传参2个函数
#     def inner(index_func):   #传参登陆函数
#         def inner2(*args,**kwargs):  #接收index的传参
#             login_func(*args,**kwargs)  #执行login函数
#             index_func(*args,**kwargs)  #执行index函数
#             quanxian_func(*args,**kwargs)  #执行quanxian函数
#         return inner2   #返回函数地址
#     return inner  #返回函数地址
# @decorator(login,quanxian)  #执行装饰器
# def index(*args,**kwargs):  #登陆函数
#     print('登陆后台！%s,%s'%(args,kwargs))
# l1 = [1,2,3,4]
# dic = {'k1':'v1','k2':'v2'}
# index(l1,dic)

lists = [([]*3) for i in range(3)]
lists[0].append(1)
lists[1].append(3)
lists[2].append(5)
print(lists)




