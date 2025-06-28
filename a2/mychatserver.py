from socket import *
import threading

# Establishing port number
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM) # TCP connection 

# Bind the server to a host and port number for connection 
serverSocket.bind(('', serverPort))
serverSocket.listen(100)

# list of connected clients 
connectedClients = []
# To avoid race condition, each client can only use print resource one at a time
clientLock = threading.Lock()

# Function to handle client message 
def handle_message(clientSocket, addr):
    while True:
        try:
            clientMsg = clientSocket.recv(1024).decode()
        except:
            break
        # Handling 'exit' condition 
        if clientMsg.lower() == 'exit':
            # Acquire the lock to prevent race condition 
            with clientLock:
                # Remove the client from the server list
                connectedClients.remove(clientSocket)
            # Close the TCP connection with the client 
            clientSocket.close()
            break

        # Relaying client message to all active clients 
        with clientLock:
            # From server list of clients 
            for client in connectedClients:
                # Message should not be relayed to sender 
                if(client != clientSocket):
                    client.send(f"{addr[1]}: {clientMsg}".encode())

while True:
    connectedSocket, addr = serverSocket.accept()
    print(f"Server listening on {addr[0]}")
    print(f"New connection from {addr[0]}: {addr[1]}")

    with clientLock:
        # Adding clients to server list 
        connectedClients.append(connectedSocket)
    threading.Thread(target=handle_message, args=(connectedSocket, addr)).start()