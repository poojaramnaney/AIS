#!/usr/bin/env python3

import socket
import time
import getpass
import socketserver
import os

def tcp_client(TCP_IP='127.0.0.1', TCP_PORT=5006, MESSAGE="Hello, World!"):
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE.encode('utf-8'))
        data = s.recv(BUFFER_SIZE).decode('utf-8')
        time1 = time.ctime()
        print(f"{time1} ---> response from {TCP_IP} : {data}")
    except ConnectionRefusedError:
        print(f"Connection to {TCP_IP}:{TCP_PORT} was refused. Ensure the server is running.")
    finally:
        s.close()


user = getpass.getuser()

def tcp_server(Host="localhost", PORT=5006):
    # Get user's home directory path, cross-platform
    user_directory = os.path.expanduser("~")
    log_path = os.path.join(user_directory, "Documents", "IDSDector.log")

    class MyTCPHandler(socketserver.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(1024).strip().decode('utf-8')
            time2 = time.ctime()
            print(f"{time2} ---> {self.client_address[0]} received the detector:")

            # Log the received message to a file
            with open(log_path, "a") as log:
                log.write(f"{time2} ---> {self.client_address[0]} received the detector: {self.data}\n")

            print(self.data)
            self.request.sendall("Successful".encode('utf-8'))

    # Start the TCP server
    server = socketserver.TCPServer((Host, PORT), MyTCPHandler)
    print(f"Server started on {Host}:{PORT}, logging to {log_path}")
    server.serve_forever()

# #!/usr/bin/env python
#
# import socket
# import time
#
# def tcp_client(TCP_IP='127.0.0.1',TCP_PORT=5006,MESSAGE="Hello, World!"):
# 	#TCP_IP = TCP_IP
# 	#TCP_PORT = TCP_PORT
# 	BUFFER_SIZE = 1024
# 	#MESSAGE = MESSAGE
#
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	s.connect((TCP_IP, TCP_PORT))
# 	s.send(MESSAGE)
# 	data = s.recv(BUFFER_SIZE)
# 	time1=time.ctime()
# 	s.close()
#
# 	print time1,"---> response from ", TCP_IP," :", data
# import getpass
# user=getpass.getuser()
# def tcp_server(Host="localhost",PORT=5006):
#
# 	import SocketServer
#
#
# 	class MyTCPHandler(SocketServer.BaseRequestHandler):
#
# 	    """
# 	    The RequestHandler class for our server.
#
# 	    It is instantiated once per connection to the server, and must
# 	    override the handle() method to implement communication to the
# 	    client.
# 	    """
#
# 	    def handle(self):
# 		global user
# 		# self.request is the TCP socket connected to the client
# 	        self.data = self.request.recv(1024).strip()
# 		time2=time.ctime()
# 	        print time2,"---> {} received the detector:".format(self.client_address[0])
# 		log=open("/home/{0}/IDSDector.log".format(user),"a")
# 		log.write("{0} ---> {1} received the detector: {2}\n".format(time2,self.client_address[0],self.data))
# 		print self.data
# 	        # just send back the same data, but upper-cased
# 	        self.request.sendall("Successful")#(self.data.upper())
#
#
# 	# Create the server, binding to localhost on port 9999
# 	server = SocketServer.TCPServer((Host, PORT), MyTCPHandler)
# 	# Activate the server; this will keep running until you interrupt the program with Ctrl-C
# 	server.serve_forever()
