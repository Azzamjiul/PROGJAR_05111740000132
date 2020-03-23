import shelve
import uuid
import socket
import os
import base64


class Dire:
    def __init__(self):
        if not os.path.exists('directory'):
            os.makedirs('directory')

    def upload_data(self, nama=None, file=None):
        makan = file
        f = open('directory/' + nama, 'wb')
        f.write(base64.decodestring(makan))
        return True

    def download_data(self, nama=None):
        array = []
        print('masuk fungsi download')
        f = open('directory/'+nama,'rb')
        l = f.read()
        print(l)
        f.close()
        hasil = base64.encodebytes(l)
        print(hasil)
        array.append(hasil.decode())
        return array

    def  list_data(self):
        lists = os.listdir('directory')
        f = []
        for filename in lists:
            f.append(filename)
        return f

if __name__=='__main__':
    dir = Dire()
    input = 'input.txt'
    print(dir.list_data())