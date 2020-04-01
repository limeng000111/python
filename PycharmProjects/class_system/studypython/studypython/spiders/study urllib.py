import urllib.request
import urllib.error
import socket
import time
# response = urllib.request.urlopen('http://www.python.org')#请求站点获得的HTTPResponse对象
# print(response.read().decode('utf-8'))  #返回网页内容
# print(response.getheader('server'))  #返回响应头的server值
# print(response.getheader())  #以元祖的形式返回响应头信息
# print(response.fileno())   #返回文件描述符
# print(response.version)   #获取所有版本信息
# print(response.status)   #返回状态码200
# print(response.debuglevel)   #返回调试等级
# print(response.closed)   #返回对象是否关闭布尔值
# print(response.geturl())  #返回检索的url
# print(response.info())  #返回网页的头信息
# print(response.getcode())   #返回响应的HTTP状态码
# print(response.msg)   #返回成功返回ok
# print(response.reason)  #返回状态信息
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
try:
#data需要字节类型的参数，使用bytes()函数转换为字节，使用urllib.parse模块中的urllib.urlencode()方法来将参数字典转换为字符串并指定其编码
    data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
    response = urllib.request.urlopen('http://www.httpbin.org/post',data = data,timeout=1)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.error):
        print('hello time out')
        print(time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time())))

#urllib.request.Request()
print('*'*20+'study'+'*'*20)
from urllib import request,parse

url = 'http://httpbin.org/post'
headers={
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}#定义头信息

dict={'name':'germey'}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=headers,method='post')
response = request.urlopen(req)
print(response.read())

#BaseHandler是其他Handler的父类   他是一个处理器，可以用来处理登录验证，处理cookies，代理设置，重定向
#密码验证
# from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
# from urllib.error import URLError
# username = 'username'
# password = 'password'
# url = 'http://localhost'
# p = HTTPPasswordMgrWithDefaultRealm()#构造密码管理实例
# p.add_password(None,url,username,password)#向实例中添加数据
#
print('*********************************')
import urllib


#私密代理授权的用户
user = "limeng"
#私密代理授权的密码
passwd = '123456'
#私密代理ip
proxyserver = '172.17.14.44'

#构造密码管理对象，用来保存需要处理的密码和账号
passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

#添加账户信息
passwdmgr.add_password(None,user,passwd,proxyserver)

#构建一个代理基础用户名|密码验证的处理器对象（ProxyBasicAuthHandler）
proxyauth_handler =urllib.request.HTTPBasicAuthHandler(passwdmgr)

#通过build_opener()方法使用这些代理handler对象
opener = urllib.request.build_opener(proxyauth_handler)

#构造http请求
request = urllib.request.Request('http://admin.democnsellers.cn/admin/Service/index')

#使用自定义opener发送请求
response = opener.open(request)

print(response.read())