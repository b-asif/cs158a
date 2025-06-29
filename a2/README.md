# Date Created 
June 28 2025

# Running the Program 
1. On your local device open a terminal to run the server. 
    python3 mychatserver.py
2. In seperate terminal windows (more than 2) execute the client program
    python3 mychatclient.py 
3. On each client end, send a message to server side. Each message will be displayed on all other 
   connected client consoles. 
4. To exit the program, the client will type 'exit' which will disconnect them from the server 
5. Server will continue to accept client requests until it is terminated manually 

# Example Execution 

SERVER
Server listening on 127.0.0.1:12000
New connection from ('127.0.0.1', 51339)
New connection from ('127.0.0.1', 51340)
New connection from ('127.0.0.1', 51341)
51341: Hi!
51340: Hello!
51339: How are you guys?
51341: Good.
51340: How about you?

CLIENT #1
Connected to chat server. Type 'exit' to leave.
Hi!

51340: Hello!

51339: How are you guys?
Good.

51340: How about you?

CLIENT #2
Connected to chat server. Type 'exit' to leave.

51341: Hi!
Hello!

51339: How are you guys?

51341: Good.
How about you?

CLIENT #3
Connected to chat server. Type 'exit' to leave.

51341: Hi!

51340: Hello!
How are you guys?

51341: Good.

51340: How about you?