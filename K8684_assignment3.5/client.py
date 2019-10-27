import socket
import sys
import os

def sendFile(socket):
    filename = 'heikkiTonni.jpg'
    file = open(filename)
    msgSize = len(file)
    dataSent = 0
    socket.send((filename+"&").encode())
    socket.send(str(len(file) + "&").encode())
    while dataSent < msgSize:
        dataSent += socket.send(file.encode())
        print('Bytes sent %d from %d' % (dataSent , msgSize))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect("localhost", 8888)
sendFile(s)
print("Files Send")
print(s.recv(1024))
s.close()