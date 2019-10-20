 
'''
[meincrab@meincrabLap K8684_assignment02]$ python server.py 
Received a connection from  ('127.0.0.1', 51946)
Length of the input: 25000 
Received 1024 out of 25000
Received 2048 out of 25000
Received 3072 out of 25000
Received 4096 out of 25000
Received 5120 out of 25000
Received 6144 out of 25000
Received 7168 out of 25000
Received 8192 out of 25000
Received 9216 out of 25000
Received 10240 out of 25000
Received 11264 out of 25000
Received 12288 out of 25000
Received 13312 out of 25000
Received 14336 out of 25000
Received 15360 out of 25000
Received 16384 out of 25000
Received 17408 out of 25000
Received 18432 out of 25000
Received 19456 out of 25000
Received 20480 out of 25000
Received 21504 out of 25000
Received 22528 out of 25000
Received 23552 out of 25000
Received 24576 out of 25000
Received 25000 out of 25000
Data received!
'''
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
    while dataRec < int(msgSize):
        data += client.recv(BUFFER_SIZE).decode()
        dataRec = len(data)
        print('Received %d out of %s'  %(dataRec,msgSize))
    print("Data received!")
    client.send(bytes("Data received\n", "utf-8"))

if __name__ == "__main__":
    main()