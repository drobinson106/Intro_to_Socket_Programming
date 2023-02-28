import socket
import os
from _thread import *

#AF_INET is the internet family for IPv4 and SOCK_STREAM is the socket type for TCP
HOST = "127.0.0.1" #localhost (IP address for a loopback interface)
PORT = 65432

#"data" is recieved from the client and .sendall(data[::-1]) sends it back in reverse
#.accepts waits for a connection "conn" then creates a new socket object for "conn"
#While loop is used to keep the connection open till it is closed by the client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((HOST,PORT)) 
s.listen(2) 
def threaded_client(conn):
	while True:
		data = conn.recv(1024)
		if not data:
			break
		conn.sendall(data[::-1])
	conn.close()
while True:
	client, address = s.accept()
	print(f"Connected by {address}")
	start_new_thread(threaded_client, (client, ))
s.close()