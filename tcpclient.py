import socket
HOST = '172.20.10.2'
PORT = 1234
input = input("message to send")
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.20.10.2', 1234))
s.send(input.encode())
data = s.recv(256)
s.close()
print('Recieved', repr(data))

