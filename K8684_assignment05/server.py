import socket
import sys
import os
BUFFER_SIZE = 1024

def parseRequest(client):
    request = ""
    while 1:
        data = client.recv(1)
        if str(data.decode()) is "&":
            break
        else:
            request += str(data.decode)
        return request

def main():
    fileFolder = (sys.argv[3])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((sys.argv[1], int(sys.argv[2])))
    sock.listen(5)

    while True:
        (client, addr) = sock.accept()
        dataRec = 0
        data = ""
        print("Received a connection from ", addr)
        print("Type of request: ")
        parseRequest(client)

        print("Name of the input: %s " % (nameOf))
        lengthOf = incomeLength(client)
        print("Length of the input: %s " % (lengthOf))
        receiveFile(client, nameOf, lengthOf, imageFolder)

if __name__ == "__main__":
    main()