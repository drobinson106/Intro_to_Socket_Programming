import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

#Creates a socket "s" that connects to the server then sends the message "Hello, world"
#"data" recieves the message from the server and prints it 
#The message is set and recieved as bytes so .decode() is used to convert bytes(b) to string(str)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024).decode()

print('Sent: Hello, world')
print('Recieved:', data)
