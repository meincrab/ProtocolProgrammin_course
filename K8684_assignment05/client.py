import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.connect((sys.argv[1], int(sys.argv[2])))
except Exception as e:
    print(e)
    print("Something is wrong with arguments!")
    sys.exit()
try: 
    s.send(bytes("hello world", "utf-8"))
except Exception as e:
    print("Something went wrong during sending Data")
    sys.exit()
print(str(s.recv(1024), "utf-8"))
s.close()