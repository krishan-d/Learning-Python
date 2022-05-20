# Socket programming with multithreading:
# To let the server interact with multiple clients you need to use multi-threading.
# server script to accept multiple client connections:


from threading import Thread
import socket


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print("received data:", data)
            conn.send(data[::-1])  # echo


TCP_IP = '0.0.0.0'  # ""
TCP_PORT = 62
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

sockTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockTcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sockTcp.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    sockTcp.listen(4)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = sockTcp.accept()
    newThread = ClientThread(ip, port)
    newThread.start()
    threads.append(newThread)

for th in threads:
    th.join()
