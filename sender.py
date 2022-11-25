import os
import socket
import time

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind((socket.gethostname(), 12345))
socket1.listen(5)

print("Host Name: ", socket1.getsockname())
client, addr = socket1.accept()

filename = input("File Name:")
filesize = os.path.getsize(filename)
client.send(filename.encode())
client.send(str(filesize).encode())

with open(filename, "rb") as file:
    c = 0
    starttime = time.time()
    while c <= filesize:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c = c + len(data)
    endtime = time.time()
print("File Transfer Complete..... Total time: ", endtime - starttime)
socket1.close()