#Quantum Age Publishing presents: Melzapp - My Personal Messenger
#SERVER
#!/usr/bin/env python3

import threading
import socket
import re
import signal   
import sys
import time

class Server():
    def __init__(self, port):
        
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind((''. port))
        self.listener.listen(10)
        print("Listening on port {0}".format(port0))

        self.client_sockets = []

        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

#MAIN LOOP
    def run(self):
        while True:
            print ("Listening for more clients")
            try:
                (client_socket, client_address) = self.listener.accept()
            except socket.error:
                sys.exit("Could not accept any more connections")
            self.client_sockets.append(client_socket)
            print("Starting client thread for {0}".format(client_address))

            client_thread = ClientListener(self, client_socket, client_address)
            client_thread.start()

            time.sleep(0.1)

#ECHO FUNCTION
    def echo(self, data):
        print("echoing: {0}".format(data))
        for socket in self.client_sockets:

            try:
                socket.sendall(data)
            except socket.error:
                print("Unable to send message")

#FINISH SERVER CLASS
    def remove_socket(self, socket):
        self.client_sockets.remove(socket)
    def signal_handler(self, signal, frame):
        print("Tidying up")
        self.listener.close()
        self.echo("QUIT")

#CLENT THREAD (New Class)
class ClientListener(threading.Thread):
    def __init__(self, server, socket, address):
        super(ClientListener, self).__init__()
        self.server = server
        self.address = address
        self.socket = socket
        self.listening = True
        self.username = "No Username"

#CLIENT THREAD'S LOOP
    def run(self):
        while self.listening:
            data = ""
            try:
                data = self.socket.recv(1024)
            except socket.error:
                "Unable to receive data"

            self.hadle_msg(data)
            time.sleep(0.1)
        print("Ending client thread for {0}".format(self.address))

#TIDYING UP
    def quit(self):
        self.listening = False
        self.socket.close()
        self.server.remove_socket(self.socket)
        self.server.echo("{0} has quit. \n".format(self.username))

#HANDLING MESSAGES
    def handle_msg(self, data):
        print("{0} sent: {1}".format(self.address, data))

        username_result = re.search('^USERNAME (.*)$', data)
        if username_result:
            self.username = username_result.group(1)
            self.server.echo("{0} has joined. \n".format(self.username))
        elif data == "QUIT":
            self.quit()
        elif data == "":
            self.quit()
        else:
            self.server.echo(data)

#STARTING THE SERVER!!!
if __name__ == "__main__":
    #Starting server on port 59091
    server = Server(59091)
    server.run()

















































