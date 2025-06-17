from socket import *

# IP address 
serverName = 'localHost'
# Port number
serverPort = 12000
# TCP socket 
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect the client socket to the server address and port 
clientSocket.connect((serverName, serverPort))

# Prompt the user to enter a sentence 
sentence = input('Input lowercase sentence: ')

# Encoding converts from string to bytes 
# Sending from client socket to server socket 
userSentence = sentence.encode('utf-8')

# Retrieve the length of the message 
msglength = len(userSentence)

# Converting the length 
stringLen = msglength.to_bytes(2, 'big')
# Send to server the string and length 
clientSocket.sendall(stringLen + userSentence)


modifiedMsg = clientSocket.recv(64)
print('From server: ', modifiedMsg.decode('utf-8'))

