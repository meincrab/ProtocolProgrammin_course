''' 

[meincrab@meincrabLap K8684_assignment3.5]$ python client.py 
Message from server: 0 of 32408 Received
Message from server: 1024 of 32408 Received
Message from server: 2048 of 32408 Received
....
....
Message from server: 26624 of 32408 Received
Message from server: 27648 of 32408 Received
Message from server: 28672 of 32408 Received
Message from server: 29696 of 32408 Received
Message from server: 30720 of 32408 Received
Message from server: 31744 of 32408 Received
Files Send
'''


import socket
import sys
import os

BUFFER_SIZE = 1024

def sendFile(socket):

    try:
        filename = (sys.argv[3])
        file = open(filename,'rb')
    except (FileNotFoundError, PermissionError):
        print("Check the file name, maybe something is wrong")
        exit()

    #open file for reading in binary format
    msgSize = os.stat(filename).st_size
    dataSent = 0
    try:
        socket.send((filename+"&").encode())
        socket.send((str(msgSize) + "&").encode())
        l = file.read(BUFFER_SIZE)
        while(l):
            socket.send(l)
            l = file.read(BUFFER_SIZE)
            print("Message from server: " + str(s.recv(BUFFER_SIZE), "utf-8"))
        file.close
    except(ConnectionError):
        print("Seems like omething went wrong on the server side")
        exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((sys.argv[1], int(sys.argv[2])))
except (ConnectionError):
    print("Something went wrong while estabilishing connection, check your props")
    exit()

sendFile(s)
print("Files Send")

s.close()