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
method = sys.argv[1]
method = str(method)
print(method)
if method == "LIST":
    list()
elif method=="DOWNLOAD":
    download( )
else:
    print("Unknown value is given as method name")


def list():
    print("Hello World")


def download():
    print("Hello World2")
