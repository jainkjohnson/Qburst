import socket
HOST = '10.5.1.144'                 
PORT = 3820
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)
conn, addr = socket.accept()
with open('myTransfer.txt', 'wb') as file_to_write:
    while True:
        data = conn.recv(1024)
        print data
        if not data:
            break
        file_to_write.write(data)
socket.close()
