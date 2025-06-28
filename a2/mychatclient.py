from socket import *
import threading

# Server Name
serverName = 'localHost'

# Port number
serverPort = 12000

# TCP connection 
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connecting the client socket to server 
clientSocket.connect((serverName, serverPort))

# Each client establishes a TCP connection and recieves messages from server 
def receive_msg():
    while True:
        receivedMsg = clientSocket.recv(1024).decode()
        if receivedMsg:
            print(f"\n{receivedMsg}")
        else:
            break


print("Connected to chat server. Type 'exit' to leave.")
threading.Thread(target=receive_msg).start()

# Client sending message to server 
while True:
    clientMsg = input()
    if(clientMsg.lower() == 'exit'):
        clientSocket.send(clientMsg.encode())
        # Close connection 
        clientSocket.close()
        print("Disconnected from server")
        break
    else:
        clientSocket.send(clientMsg.encode())