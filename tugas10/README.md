# Tugas 10 Pemrograman Jaringan

## Menjalankan Service

### Setelah pull update terbaru

### Menjalankan async_server.py dengan port 9002, 9003, 9004, 9005

![alt text](capture/all_server.png)

### Menjalankan file lb.py dan menjalankan di port 44444

![alt text](capture/load_balancer.png)


### Mengakses http://localhost:44444/page.html pada browser

![alt text](capture/page.png)

### Mengecek dan melihat proses di log program bahwa setiap request akan dilayani oleh backend secara bergantian

![alt text](capture/load_balancer_log.png)


## Hasil performance test

### ab -n 1000 -c 1 -r http://127.0.0.1:44444/

![alt text](capture/1.png)

### ab -n 1000 -c 10 -r http://127.0.0.1:44444/

![alt text](capture/10.png)

### ab -s 200 -n 1000 -c 100 -r http://127.0.0.1:44444/

![alt text](capture/100.png)

### ab -s 200 -n 1000 -c 500 -r http://127.0.0.1:44444/

![alt text](capture/500.png)

### ab -s 200 -n 1000 -c 1000 -r http://127.0.0.1:44444/

![alt text](capture/1000.png)