import socket

SERVER_IP = "192.168.65.1"
PORT = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
 
def send_message(msg):
    client.send(str.encode(msg))
    print(client.recv(2048).decode("utf-8"))
 
send_message("Hello Server!")