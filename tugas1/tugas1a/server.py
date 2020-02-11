import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 31000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection hoho')

    connection, client_address = sock.accept()
    print(sys.stderr, 'connection from ', client_address)

    # Receive file
    i = 1
    file = open('file_'+ str(i)+".pdf",'wb') # Open in binary
    i = i + 1

    while True:
        data = connection.recv(1024)
        # print(sys.stderr, 'received ', data)
        while(data):
            file.write(data)
            data = connection.recv(1024)
    file.close()

    # Clean up the connection
    connection.close()
