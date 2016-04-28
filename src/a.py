from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connetction'
    conn, addr = tcpSerSock.accept()
    print '...connetcted from:', addr

    while True:
        data = conn.recv(BUFSIZ)
        if not data:
            break
        conn.send('[%s] %s' % (ctime(), data))

        conn.close()
tcpSerSock.close()
