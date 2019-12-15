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



def listFiles(socket):
    socket.send(("LIST\n").encode())
def downloadFile(socket):
    print("Hello World2")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
method = ""
try:
    method = sys.argv[1]
except Exception as e:
    print("ValueError - check your arguments ")
    exit()
method = str(method)

try:
    sock.connect((sys.argv[2], int(sys.argv[3])))
except (ConnectionError):
    print("Something went wrong while estabilishing connection, check your props")
    exit()

if method == "LIST":
    listFiles(sock)
elif method=="DOWNLOAD":
    downloadFile(sock)
else:
    print("Unknown value is given as method name")

