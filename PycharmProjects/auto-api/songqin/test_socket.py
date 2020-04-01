import socket
import sys

#创建一个socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本机地址
host = socket.gethostname()

#设置端口号
port = 9999

#绑定(设置元祖）
serversocket.bind((host,port))

#设置最大连接数
serversocket.listen(5)

while True:
    clientserver,addr = serversocket.accept()
    print('addr%s'%str(addr))
    print('clientserver%s'%str(clientserver))
    msg = 'hello , I am server'
    clientserver.send(msg.encode('utf-8'))
    clientserver.close()


