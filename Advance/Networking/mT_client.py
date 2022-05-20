import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 1024
MESSAGE = str(input())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send(MESSAGE.encode())
# receive data from the server and decoding to get the string.
data = s.recv(BUFFER_SIZE).decode()
print("Received data :", data)

# close the connection
s.close()
