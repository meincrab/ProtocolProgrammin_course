import socket
import sys

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

'''
[meincrab@meincrabLap K8684_assignment03]$ python server.py "localhost" 8888
Received a connection from  ('127.0.0.1', 52210)
hello world
Received a connection from  ('127.0.0.1', 52212)
hello world
Received a connection from  ('127.0.0.1', 52214)
hello world
'''


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Allows not to wait and avoid "Port already in use " error, handy
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind((sys.argv[1], int(sys.argv[2])))
    except Exception as e:
        print(e)
        print("Something is wrong with arguments!")
        sys.exit()
    while 1:
        sock.listen(5)
        (client, addr) = sock.accept()
        print("Received a connection from ", addr)
        print(str(client.recv(1024), "utf-8"))
        client.send(bytes("Data received\n", "utf-8"))

if __name__ == "__main__":
    main()