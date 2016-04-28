# coding:utf-8
import socket
import time

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 定义socket类型，网络通信，TCP
s.bind(ADDR) # 套接字绑定的IP与端口
s.listen(5) # 开始TCP监听

while True:
    print 'waiting for connetction'
    conn, addr = s.accept()   # 接受TCP连接，并返回新的套接字与IP地址
    print '...connetcted from:', addr

    while True:
        data = conn.recv(BUFSIZ)  # 把接收的数据实例化
        if not data:
            break
        conn.sendall('[%s] %s' % (time.ctime(), data))
        # conn.close()
s.close()
