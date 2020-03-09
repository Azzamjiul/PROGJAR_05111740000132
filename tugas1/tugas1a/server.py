import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 31000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(10)
while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for connection')
    connection, client_address = sock.accept()
    print('Connection from')
    f = open('terkirim'".pdf", "wb")
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        while (data):
            f.write(data)
            data = connection.recv(1024)
        f.close()

        # Clean up the connection
    connection.close()