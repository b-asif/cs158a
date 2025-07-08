# Date Created
July 6 2025 

# Config file
Each process (host) must have its own config.txt file that is structured as such: 
<serverIP><serverPort> e.g. 10.1.1.1,5001
<clientIP><clientPort> e.g. 10.1.1.2,5001
<processNumber>        e.g. 1


# Running the Program 
1. Open three terminal tabs and run the following:
    python3 myleprocess.py config1.txt
    python3 myleprocess.py config2.txt
    python3 myleprocess.py config3.txt
2. Each process will log to corresponding log file (log1.txt, log2.txt, log3.txt)
3. When the leader is elected, it will be displayed on console as 
    Leader is <leader_id>
    # example
    Leader is eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73

# Example Execution 

config3:

python3 myleprocess.py config3.txt
the server IP is  127.0.0.1 and serverPort is  5003
the client IP is  127.0.0.1 and clientPort is  5001
Server not ready for connection, retrying connection again.
Leader is d6001c44-56d2-4636-b7f7-e51c09297559

Log3: 
Sent: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=0
Received: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=0, same, 0
Leader is decided to eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73.
Sent: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=1
Received: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=1, same, 1

config1.txt:

python3 myleprocess.py config1.txt
the server IP is  127.0.0.1 and serverPort is  5001
the client IP is  127.0.0.1 and clientPort is  5002
Leader is eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73

Log1: 
Received: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=0, greater, 0
Sent: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=0
Received: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=1, greater, 0
Leader is decided to eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73.
Sent: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=1

config2.txt:

python3 myleprocess.py config2.txt
the server IP is  127.0.0.1 and serverPort is  5002
the client IP is  127.0.0.1 and clientPort is  5003
Leader is eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73

Log2:
Received: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=0, greater, 0
Sent: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=0
Received: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=1, greater, 0
Leader is decided to eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73.
Sent: uuid=eb9d3dbb-8ac3-4695-8d3e-8b5f1c933a73, flag=1

