from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSliSock = socket(AF_INET, SOCK_STREAM)
tcpSliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpSliSock.send(data)
    data = tcpSliSock.recv(BUFSIZE)
    if not data:
        break
tcpSliSock.close()
