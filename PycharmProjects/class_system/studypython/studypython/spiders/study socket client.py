#客户端代码
import socket
hostport = ('127.0.0.1',8888)
#创建TCP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(hostport)  #链接套接字

while True:
    user_input = input('>>>').strip()
    s.send(bytes(user_input,'utf-8'))#发送数据到套接字
    if not len(user_input):continue
    if user_input == 'quit':
        s.close()
        break
    server_reply = s.recv(1024) #接受套接字数据

    print(str(server_reply,'utf-8'))

import socketserver

