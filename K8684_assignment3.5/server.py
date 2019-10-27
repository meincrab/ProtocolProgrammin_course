'''
[meincrab@meincrabLap K8684_assignment3.5]$ python server.py 
Received a connection from  ('127.0.0.1', 34330)
Name of the input: heikkiTonni.jpg 
Length of the input: 32408 
1024 of 32408 Received
2048 of 32408 Received
3072 of 32408 Received
...
...
...
29696 of 32408 Received
30720 of 32408 Received
31744 of 32408 Received
32408 of 32408 Received
Receiving done
'''
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

    '''
    Just to remember, can be useful in future
    if not os.path.exists(folder)
        os.makedirs(folder)
    '''    
    if not os.path.exists(folder):
        print("Seems like folder is missing")
        client.send(bytes("Server error", "utf-8"))
        client.close 
        exit()

    print("Folder exists!")
    file = open(os.path.join(folder, name), 'wb')      
    received = 0
    l = client.recv(BUFFER_SIZE)
    client.send(bytes("%d of %s Received" % (received, length), "utf-8"))  
    try:
        while(l):
            received += len(l)
            file.write(l)
            l = client.recv(BUFFER_SIZE)
            print ("%d of %s Received" % (received, length))
            client.send(bytes("%d of %s Received" % (received, length), "utf-8"))  
        file.close()
        print("Receiving done")
    except Exception as e:
        print("Something went wrong during data transfer")
        client.send(bytes("Server error", "utf-8"))
        client.close 
        exit()



def main():
    imageFolder = (sys.argv[3])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Allows not to wait and avoid "Port already in use " error 
    sock.bind((sys.argv[1], int(sys.argv[2])))
    sock.listen(5)
    
    while True:
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