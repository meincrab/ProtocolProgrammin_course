import socket# Create the socket
import sys

#Reading from file allowed to speed up debugging process significantly.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dataFile = open("data.txt", "r")
dataString = dataFile.read()


# I'm not sure if it was allowed to use sendall...
'''
def  sendDataSimbple(s, data)
    try:
        s.connect(("localhost", 5005))
    except:
        print("Something went wrong. Connection didn't succeed")
    else:
        print("Connection successfull")
        try:
                sent = s.sendall(data.encode())
                print(str(s.recv(1024), "utf-8"))
        except: 
            print("Didnt succeed to send data")
        else:
            print("Data sent successfully")
    
    s.close

'''


# ... So I made a few versions
def sendData(s, data):
    try:
        s.connect(("localhost", 5005))
    except:
        print("Something went wrong. Connection didn't succeed")
    else:   
        print("Connection successfull")
        try:
            dataSent = 0
            dataSize = len(data)
            startSlice = 0
            stopSlice = 1025
            print('Datasize is : ' + str(dataSize))
            while(dataSent < dataSize):
                if(dataSize <= 1024):
                    sent = s.send(data.encode())
                    print('Bytes sent : ' + str(sent))
                    print(str(s.recv(1024), "utf-8"))
                    dataSent += sent
                else:
                    sObject = slice(startSlice, stopSlice)
                    dataToSend = data[sObject]
                    sent = s.send(dataToSend.encode())
                    print(str(s.recv(1024), "utf-8"))
                    print(dataSent)
                    dataSent += sent
                    print(startSlice)
                    print(stopSlice)
                    #Python allows slicing with index out of range, so no extra checks neeeded
                    stopSlice += 1024
                    startSlice += 1024 
        except: 
            print("Didnt succeed to send data")
        else:
            print("Data sent successfully")
            print("Bytes to send: " + str(dataSize))
            print("Bytes sent " + str(dataSent))
    
    s.close

sendData(s, dataString)