
import socket
import random


class main_client():

    IP = socket.gethostbyname(socket.gethostname())
    # PORT = random.randint(1100, 65535)
    PORT = 65535
    ADDR = (IP, PORT)
    FORMAT = "utf-8"
    SIZE = 1024

    # Chạy TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Kết nối đến server
    client.connect(ADDR)

    # Mở đọc dữ liệu
    file = open("data/data.txt", "r")
    data = file.read()

    # Gửi file đến server
    client.send("data/data.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Truyền data đến server
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    file.close()
    client.close()
