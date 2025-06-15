from socket import *
import struct

#port number 
serverPort = 12000
#socket object is created when we use the socket method 
serverSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREM for TCP connection

#bind the server to a host and port number for connection 
serverSocket.bind(('', serverPort))
serverSocket.listen(100)

while True:
    #address will be the port number and IP address of the client 
    connectedSocket, addr = serverSocket.accept()
    #addr[0] is the IP address and addr[1] is the client port number
    print(f"Connected from {addr[0]}") #printing the address of the connected client 
    
    #the first two bytes of the string is the length of the string
    stringLength = connectedSocket.recv(2)
    length = (stringLength[0] << 8) | stringLength[1]
    print(f"msg_length: ", length)

    #retrieve the actual message 
    inputData = b''
    while len(inputData) < length:
        userString = connectedSocket.recv(min(64, length - len(inputData)))
        inputData += userString
    
    print('processed:', inputData.decode())

    #capitalize the input 
    capSentence = inputData.upper()
    connectedSocket.send(capSentence)
    print(f'msg_length_sent: ', length)
    print('Connection closed')
    connectedSocket.close()


