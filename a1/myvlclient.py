from socket import *

# ip address 
serverName = 'localHost'
# port number
serverPort = 12000
# tcp socket 
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect the client socket to the server address and port 
clientSocket.connect((serverName, serverPort))

# prompt the user to enter a sentence 
sentence = input('Input lowercase sentence: ')

# encoding converts from string to bytes 
# sending from client socket to server socket 
userSentence = sentence.encode('utf-8')

# retrieve the length of the message 
msglength = len(userSentence)

# converting the length 
stringLen = msglength.to_bytes(2, 'big')
# send to server the string and length 
clientSocket.sendall(stringLen + userSentence)


modifiedMsg = clientSocket.recv(64)
print('From server: ', modifiedMsg.decode('utf-8'))

