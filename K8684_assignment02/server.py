 
import socket

BUFFER_SIZE = 1024

def incomeLength(client):
    length = ""
    while 1:
        data = client.recv(1)
        if str(data.decode()) is "&":
            break
        else: 
            length += str(data.decode())
    return length


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Allows not to wait and avoid "Port already in use " error
    
    sock.bind(("localhost", 8888))
    sock.listen(5)
    (client, addr) = sock.accept()
    dataRec = 0
    data = ""  
    print("Received a connection from ", addr)
    msgSize = incomeLength(client)
    print("Length of the input: %s " % (msgSize))
    while 1:
        data += client.recv(BUFFER_SIZE).decode()
        dataRec = len(data)
        print('Received %d out of %s'  %(dataRec,msgSize))
        print(data)
    print (str(client.recv(1024), "utf-8"))
    client.send(bytes("Data received\n", "utf-8"))

if __name__ == "__main__":
    main()