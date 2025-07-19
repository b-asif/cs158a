import uuid
import socket
import threading
import time
import json
import sys

# Message Class 
class Message:
    def __init__(self, processUUID, flag):
        # UUID indicating the sender's UUID.
        self.uuid = str(processUUID)
        # representing if the leader is already elected.
        self.flag = flag
        # Converting to JSON to serialize the Message instances
    def convertToJson(self):
        # Converting python object into JSON-formatted string 
        return json.dumps({
            "uuid": self.uuid,
            "flag": self.flag
        })
    # Create a Message instance from a JSON string (deserialization)
    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Message(data["uuid"], data["flag"])


# From config file, retrieve the server and client connection information 
def config():
    # Use first command-line arg after file name as config file name 
    # default to config.txt if no file is provided by user  
    config_fileName = sys.argv[1] if len(sys.argv) > 1 else "config.txt"
    
    with open(config_fileName, "r") as file:
        # Read all lines of file 
        lines = file.readlines()
    # Extracting the server's IP and port number from the first line of the file 
    serverIP, serverPort = lines[0].strip().split(",")

    # Extracting the client's IP and port number from the second line of the file 
    clientIP, clientPort = lines[1].strip().split(",")

    # Log the IP and Port numbers to console for verification  
    print("the server IP is ",serverIP, "and serverPort is ",serverPort)
    print("the client IP is ",clientIP, "and clientPort is ",clientPort)

    return(serverIP, int(serverPort)), (clientIP, int(clientPort))

# Establishing server side connection
# handle incoming messages from the client 
def server_connection(serverIP, serverPort, recieve):
    # TCP connection 
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind socket to the provided IP address and Port number  
    serverSocket.bind((serverIP, serverPort))
    
    # Listen for incoming connections 
    serverSocket.listen(1)
    connectedSocket, add = serverSocket.accept()
    
    while True:
        # Recieve data from the client 
        data = connectedSocket.recv(1024)
        if not data:
            # Handler for when the client disconnects 
            break
        # Sending the data to message function
        message = Message.from_json(data.decode()) 
        recieve(message)

    # Close the connection 
    connectedSocket.close() 

# Establishing client side connection 
def client_connection(clientIP, clientPort):
    while True:
        try:
            # TCP socket  
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Attempt to connect to server IP and port 
            clientSocket.connect((clientIP, clientPort))
            
            # If connection is successful return the socket 
            return clientSocket
        except:
            # If connection failed, retry after 2 seconds  
            print("Server not ready for connection, retrying connection again.")
            time.sleep(2)

# When a process receives a message, it should clearly show, on a log file
def log(logfile, msg):
    with open(logfile, "a") as file:
        file.write(msg + "\n")

def main():
    (serverIP, serverPort), (clientIP, clientPort) = config() 
    processID = uuid.uuid4() # Generate unique id for process 
    electionStatus = 0 # Election status = 0, leader not known. 1 = known 
    leader_id = None
    client = None
    logFile = f"log{clientPort}.txt"

    # Server calls this function everytime a message is recieved 
    def msg_received(msg):
        # Modify the following variables depending on status 
        nonlocal electionStatus, leader_id, client
        while client is None:
            time.sleep(0.1)
        # Update leader status based on incoming messages from neighbors  
        recieved_UUID = uuid.UUID(msg.uuid)
        # Comparing sender's UUID with this process's UUID 
        
        if recieved_UUID > processID:
            current = "greater"
        elif recieved_UUID < processID:
            current = "less"
        else:
            current = "same"
        # Log format for current state and leader info
        currentState = "1" if electionStatus else "0"
        logEntry = f"Received: uuid={msg.uuid}, flag={msg.flag}, {current}, {currentState}"
        log(logFile, logEntry)

        # Handle leader announcement or continue election based on flag 
        if msg.flag == 1:
            # Updating leader state 
            if electionStatus == 0:
                leader_id = recieved_UUID
                electionStatus = 1
                log(logFile, f"Leader is decided to {leader_id}.")
            # Forwarding that the leader has been chosen 
            if recieved_UUID != processID:

                forward_msg = Message(leader_id, 1)
                client.sendall(forward_msg.convertToJson().encode())
                log(logFile, f"Sent: uuid={forward_msg.uuid}, flag={forward_msg.flag}")
        # Still electing a leader
        elif msg.flag == 0:
            # If your UUID is sent back to you then you are the leader 
            if recieved_UUID == processID:
                # This process's UUID has returned — declare self as leader
                electionStatus = 1

                # Set this process UUID as leader ID
                leader_id = processID
                
                # Log to file 
                log(logFile, f"Leader is decided to {leader_id}.")
                
                # Forward to neighbors that leader has been elected 
                forward_msg = Message(leader_id, 1)
                client.sendall(forward_msg.convertToJson().encode())
                log(logFile, f"Sent: uuid={forward_msg.uuid}, flag=1")

                # If sender UUID is greater than this process UUID - forward 
            elif recieved_UUID > processID:
                client.sendall((msg.convertToJson() + "\n").encode())
                # Still trying to find the leader 
                log(logFile, f"Sent: uuid={msg.uuid}, flag=0")
            else:
                # Ignore messages from lower UUIDs (no forwarding)
                log(logFile, f"Ignored message from: uuid={msg.uuid}")

    # Start server thread to accept connection from left neighbor    
    threading.Thread(target=server_connection, args=(serverIP, serverPort, msg_received), daemon=True).start() 
    # Time for server to respond 
    time.sleep(1)
    # Connect to right neighbor's server as a client
    client = client_connection(clientIP, clientPort)
    time.sleep(1)

    # Initial message being sent with this process UUID 
    if electionStatus == 0:
        msg = Message(processID, 0)
        client.sendall(msg.convertToJson().encode())
        log(logFile, f"Sent: uuid={msg.uuid}, flag={msg.flag}")
        
    # Wait until this process knows the elected leader
    while electionStatus == 0:
        time.sleep(2)
    
    print(f"Leader is {leader_id}")
    
    # Run the program 
if __name__ == "__main__":
     main()
    
    


            









