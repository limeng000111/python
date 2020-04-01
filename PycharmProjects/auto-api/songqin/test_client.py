import socket
import sys

#创建对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本机地址
host = socket.gethostname()

#端口
port = 9999

#连接服务端
s.connect((host,port))

#设置接收最大数值
msg = s.recv(1024)

#关闭连接
s.close()

print(msg.decode('utf-8'))
