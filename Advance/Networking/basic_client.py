import socket


TCP_IP = '127.0.0.1'
# Define the port on which you want to connect
# The port on which our server runs
TCP_PORT = 63000
BUFFER_SIZE = 1024
MESSAGE = "Hi Eve!"

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server on local computer
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
# receive data from the server and decoding to get the string.
data = s.recv(BUFFER_SIZE).decode()
print("Received data :", data)
# close the connection
s.close()
