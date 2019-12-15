import socket
import sys
import os
BUFFER_SIZE = 1024

def parseRequest(client):
    print(client)
    request = ""
    while 1:
        data = client.recv(1)
        print(data)
        if str(data.decode()) is "&":
            break
        else:
            request += str(data.decode)
        return request

def main():
    fileFolder = (sys.argv[1])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((sys.argv[2], int(sys.argv[3])))
    sock.listen(5)

    while True:
        (client, addr) = sock.accept()
        dataRec = 0
        data = parseRequest
        print("Received a connection from ", addr)
        requestType =  parseRequest(client)
        print("Type of request: " + requestType)

if __name__ == "__main__":
    main()