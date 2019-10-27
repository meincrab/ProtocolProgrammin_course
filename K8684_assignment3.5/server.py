import socket
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


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Allows not to wait and avoid "Port already in use " error 
    sock.bind(("localhost", 8888))
    sock.listen(5)
    (client, addr) = sock.accept()

    



if __name__ == "__main__":
    main()