from socket import *
import struct

# Port number 
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM) # SOCK_STREM for TCP connection

# Bind the server to a host and port number for connection 
serverSocket.bind(('', serverPort))
serverSocket.listen(100)

while True:
    # Address will be the port number and IP address of the client 
    connectedSocket, addr = serverSocket.accept()
    # Addr[0] is the IP address and addr[1] is the client port number
    print(f"Connected from {addr[0]}") #printing the address of the connected client 
    
    # The first two bytes of the string is the length of the string
    stringLength = connectedSocket.recv(2)
    # Converting from 2 byte big-endian to int value  
    length = (stringLength[0] << 8) | stringLength[1]
    print(f"msg_length: ", length)

    # Retrieve the string message 
    inputData = b''
    while len(inputData) < length:
        userString = connectedSocket.recv(min(64, length - len(inputData)))
        inputData += userString
    
    print('processed:', inputData.decode())

    # Capitalize the input 
    capSentence = inputData.upper()

    connectedSocket.send(capSentence) # Send the capitalized message back to the client
    print(f'msg_length_sent: ', length)
    print('Connection closed')
    connectedSocket.close()


