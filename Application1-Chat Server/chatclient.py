import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter the host name of the server: "))
port = 8080

s.connect((host, port))
print("Connected with the server")

while 1:
        
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ",incoming_message)
    print("")
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("Message has been sent!")
    print("")
