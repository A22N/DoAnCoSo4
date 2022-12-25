import socket


sock = socket.socket()
print("Socket created successfully.")


port = 8800
host = 'localhost'


sock.connect((host, port))
print('Connection Established.')

sock.send('A message from the client'.encode())

file = open('client-file.txt', 'wb')

line = sock.recv(1024)

while (line):
    file.write(line)
    line = sock.recv(1024)

print('File has been received successfully.')

file.close()
sock.close()
print('Connection Closed.')
