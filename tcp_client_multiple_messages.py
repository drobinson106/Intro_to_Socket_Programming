import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

#Creates a socket "s" that connects to the server then sends a user inputted "message"
#"data" recieves the message from the server and prints it 
#The message must be sent and recieved as bytes so .decode() is used to convert bytes(b) to string(str) and the reverse for .encode()
#While loop used to keep the connection open until user inputs "end" which closes the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
	message = input("\nWhat's your message : ")
	s.sendall(message.encode())
	data = s.recv(1024).decode()
	print(message)
	print('Recieved:', data)
	if message == 'end':
		break
	else:
		continue