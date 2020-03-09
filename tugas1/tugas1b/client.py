import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 31000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.connect(server_address)

with open('terkirim.pdf', 'wb') as f:
    print("file opened")
    while True:
        print("receiving data...")
        data = sock.recv(1024)
        print('data=%s', (data))
        f.write(data)
        if not data:
            f.close()
            break

print("success")
sock.close()