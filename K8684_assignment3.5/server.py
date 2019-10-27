import socket
import sys
import os
BUFFER_SIZE = 1024

def fileName(client):
    name = ""
    while 1:
        data = client.recv(1)
        if str(data.decode()) is "&":
            break
        else: 
            name += str(data.decode())
    return name

def incomeLength(client):
    length = ""
    while 1:
        data = client.recv(1)
        if str(data.decode()) is "&":
            break
        else: 
            length += str(data.decode())
    return length

def receiveFile(client, name, length, folder):
    #open file for writing in binary format
    file = open(os.path.join(folder, name), 'wb')
    received = 0
    l = client.recv(BUFFER_SIZE)
    while(l):
        received += len(l)
        print("receiving")
        file.write(l)
        l = client.recv(BUFFER_SIZE)
        print (" %d of %s Received" % (received, length))
    print("Receiving done")
    file.close()



def main():
    imageFolder = "received-files"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Allows not to wait and avoid "Port already in use " error 
    sock.bind(("localhost", 8888))
    sock.listen(5)
    (client, addr) = sock.accept()
    dataRec = 0
    data = ""
    print("Received a connection from ", addr)
    nameOf = fileName(client)
    print("Name of the input: %s " % (nameOf))
    lengthOf = incomeLength(client)
    print("Length of the input: %s " % (lengthOf))
    receiveFile(client, nameOf, lengthOf, imageFolder)

    



if __name__ == "__main__":
    main()