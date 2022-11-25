import os
import socket
import time

host = input("Host Name: ")
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket1.connect((host, 12345))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

filename = socket1.recv(100).decode()
filesize = socket1.recv(100).decode()

with open("./received files/" + filename, "wb") as file:
    c = 0
    starttime = time.time()
    while c <= int(filesize):
        data = socket1.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)
    endtime = time.time()

print("File transfer Complete..... Total time: ", endtime - starttime)
socket1.close()