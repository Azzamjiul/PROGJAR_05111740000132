import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 31000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(10)

while True:
    connection, address = sock.accept()
    print('Connection from', address)

    f = open("null.pdf", 'rb')
    isi = f.read(1024)
    while (isi):
        connection.send(isi)
        isi = f.read(1024)
    f.close()

    print('Done Sending')
    connection.close()