 
import socket


def sendMessage(socket):
    msg = msgGen("Hello")
    msgSize = len(msg)
    dataSent = 0
    socket.send((str(msgSize)+"&").encode())
    while dataSent < msgSize:
        dataSent += socket.send(msg.encode())
        print('Bytes sent %d from %d' % (dataSent , msgSize))

def msgGen(message):
    return message * 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8888))
sendMessage(s)
print(str(s.recv(1024), "utf-8"))
s.close()