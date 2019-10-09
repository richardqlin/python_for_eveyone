from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('data.pr4e.org',80))

cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.1\n\n".encode()
s.send(cmd)

while 1:
    data = s.recv(1024)
    if len(data) < 1:
        break
    print(data.decode())

s.close()

