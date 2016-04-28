import socket

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR) # 要连接的IP与端口

while True:
    data = raw_input('> ')
    if not data:
        break
    s.send(data)
    data = s.recv(BUFSIZE) # 把接收的数据定义为变量
    print data
s.close()
