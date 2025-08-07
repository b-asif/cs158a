import socket
import ssl

hostname = "www.google.com" # Connecting to domain 
port = 443 # default HTTP port 

# Creating a default SSL connection 
context = ssl.create_default_context()

# Creating a TCP connection to Google server on port 443 
with socket.create_connection((hostname, port)) as sock:
    # Wrapping the TCP connection with SSL to create a secure connection 
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        # GET request 
        request = (
            "GET / HTTP/1.1\r\n" # Request line with GET method - HTTP/1.1 is commonly used for GET request 
            f"Host: {hostname}\r\n" # \r\n will indicate the end of HTTP header line  
            "Connection: close\r\n\r\n" # Close the server connection after the response has been received 
                                        # Indicate end of header section 
        )

        ssock.sendall(request.encode())
        # Receives the HTTP response from the server
        response = b""
        # Keep reading the data until there is nothing left 
        while True:
            dataRecieved = ssock.recv(4096)
            if not dataRecieved:
                break
            # Add recieved data to response 
            response += dataRecieved
# Taking the response from the HTTP get request and converting into string
response_decode = response.decode(errors='ignore')
# 'header' will hold the index where the HTTP header ends 
header = response_decode.find("\r\n\r\n") # Body of the HTTP GET request will start after header
# Body of the GET request is after the header 
html = response_decode[header+4: ]

# Saves the complete HTML content of the response to a file named response.html
with open("response.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML content of the response saved to a file named response.html")
