import socket


s = socket.socket()
print("Socket successfully created")

# we have not typed any ip in the ip field instead we have inputted an empty string
# this makes the server listen to requests coming from other computers on the network.
TCP_IP = ''
# reserve a port on your computer in our
# case it is 63000, but it can be anything
TCP_PORT = 63000
BUFFER_SIZE = 1024

# Next bind to the port
s.bind((TCP_IP, TCP_PORT))
print("socket bound to %s" % TCP_PORT)

# put the socket into listening mode
# 1 here means that 1 connection is kept waiting if the server is busy and
# if a 2nd socket tries to connect then the connection is refused.
s.listen(1)
print("socket is listening")


while True:
    # Establish connection with client.
    c, add = s.accept()
    print('Got connection from', add)

    data = c.recv(BUFFER_SIZE).decode()
    if not data: break
    print("Received data :", data)
    # send a message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())

# Close the connection with the client
c.close()


# start the server
# $ python server.py

# keep the above terminal open
# now open another terminal and type:
# $ telnet localhost 63000
