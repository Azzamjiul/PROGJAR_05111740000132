import logging
import requests
import threading
import datetime
import os

threads = []


def download_gambar(url=None, nama=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/jpeg'] = 'jpg'

    currentDT = datetime.datetime.now()
    currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = nama
        ekstensi = tipe[content_type]
        logging.warning(f"\n Download {namafile}.{ekstensi},\n Date = {currentDT} ")
        logging.warning(f"\n Download {namafile}.{ekstensi},\n Date = {currentDT} ")
        fp = open(f"{namafile}.{ekstensi}", "wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__ == '__main__':

    x = threading.Thread(target=download_gambar, args=(
    'https://asset.kompas.com/crops/KXo69E4A7E02SZq4pt4A3gxvI6k=/0x0:1000x667/750x500/data/photo/2020/02/20/5e4e0f6cd3e7f.jpg',
    'Foto_Ke-1',))
    threads.append(x)
    x = threading.Thread(target=download_gambar, args=(
    'https://asset.kompas.com/crops/cJzoLGQQwzUU8RZfISjB5C0c0Zw=/0x41:1000x708/177x117/data/photo/2020/03/01/5e5b66c42d2f1.jpg',
    'Foto_Ke-2',))
    threads.append(x)
    x = threading.Thread(target=download_gambar, args=(
    'https://asset.kompas.com/crops/_SYW7qEZ5oWW5lkr9xFSoWtQVVM=/0x0:490x327/177x117/data/photo/2020/02/15/5e47f230b8e93.jpg',
    'Foto_Ke-3',))
    threads.append(x)

    for i in threads:
        i.start()