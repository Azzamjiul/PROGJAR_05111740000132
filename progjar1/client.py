import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8000)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    # print >>sys.stderr, 'sending "%s"' % message
    print(sys.stderr, 'sending ', message)
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    # print "%d" % amount_expected
    # print(amount_expected)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        # print "amount_received = %d" % amount_received
        # print >>sys.stderr, 'received "%s"' % data
        print(sys.stderr, 'received "%s"' % data)
finally:
    # print >>sys.stderr, 'closing socket'
    print(sys.stderr, 'closing socket')
    sock.close()
