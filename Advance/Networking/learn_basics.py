# Socket programming:
# Way of connecting two nodes on a network to communicate with each other.
# server and client.

# importing socket and making simple socket:

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET refers Address-Family ipv4.
# SOCK_STREAM means connection oriented TCP protocol.

# Connecting to a server:
# when any error occurs during the creation of a socket then a socket.error is thrown,
# and we can only connect to a server by knowing its IP.
# Find server ip using:
# $ ping www.google.com
# or

# ip = socket.gethostbyname('www.google.com')
# print(ip)

# Example 1:
import learn_basics
import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % err)


port = 80  # default port for socket

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("The socket has successfully connected to google")
s.close()
