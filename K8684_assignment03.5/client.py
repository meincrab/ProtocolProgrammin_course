import socket
import sys


def sendImage(socket):
    imgAddr = '/imageSend/heikkiTonni.jpg'
    file = open(imgAddr)
    length = file.read(1024)
    while(length):
        print("Sending::")
        s.send(length)
        length = file.read(1024)
    file.close()
    print("Sending Done")

def sendData(size,name):
    




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect("localhost", 8888)
sendImage(s)
print(s.recv(1024))
s.close()