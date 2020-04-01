#!/usr/bin/python
#-*—coding:UTF-8-*-
import socket

#创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HostPort = ('127.0.0.1',8888)
s.bind(HostPort)  #绑定地址端口
s.listen(5)   #监听个数
while True:
    print('server socket waiting...')
    c,addr = s.accept() #阻塞等待连接，创建套接字c链接和地址信息addr
    while True:
        try:
            client_data = c.recv(1024)  #接受客户端的数据，来自客户端的数据类型为bytes，需要转换为str
            if str(client_data,'utf-8') == quit:
                c.close()
                break
        except Exception:
            break
        c.send(client_data) #发送数据给客户端
        print('clientINFO:',str(client_data,'utf-8'))

