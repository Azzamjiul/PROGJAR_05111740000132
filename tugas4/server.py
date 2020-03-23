from socket import *
import socket
import threading
import logging
import sys
from file_machine import FileMachine
pm = FileMachine()


class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        file = (b'')
        test = []
        while True:
            while True:
                data = self.connection.recv(1024)
                file = file + data
                test.append(data)
                byte = int(sys.getsizeof(data))

                if byte != 1057:
                    print(byte)
                    break
                else:
                    print(byte)
                    self.connection.sendall(b'halo')
            data = file
            if data:
                d = data.decode()
                result = pm.process(d)
                result = result
                self.connection.sendall(result.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8889))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f'connection from {self.client_address}')

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    print('Menjalankan server ....')
    svr = Server()
    svr.start()


if __name__ == '__main__':
    main()