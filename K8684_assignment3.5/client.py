import socket
import sys
import os

BUFFER_SIZE = 1024

def sendFile(socket):
    filename = 'heikkiTonni.jpg'
    #open file for reading in binary format
    file = open(filename,'rb')
    msgSize = os.stat(filename).st_size
    dataSent = 0
    socket.send((filename+"&").encode())
    socket.send((str(msgSize) + "&").encode())
    l = file.read(BUFFER_SIZE)
    while(l):
        socket.send(l)
        l = file.read(BUFFER_SIZE)
    file.close

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8888))
sendFile(s)
print("Files Send")
print(s.recv(BUFFER_SIZE))
s.close()