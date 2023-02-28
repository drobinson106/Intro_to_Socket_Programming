import socket

HOST = "127.0.0.1" #localhost (IP address for a loopback interface)
PORT = 65432

#AF_INET is the internet family for IPv4 and SOCK_STREAM is the socket type for TCP
#.accepts waits for a connection "conn" then creates a new socket object for "conn"
#"data" is recieved from the client and .sendall(data.upper()) sends it back in all uppercase
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
	s.bind((HOST,PORT)) 
	s.listen() 
	conn, addr = s.accept()
	with conn:
		print(f"Connected by {addr}")
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data.upper())
