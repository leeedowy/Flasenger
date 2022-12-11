import socket
from message import Message


PAYLOAD_MAX_SIZE = 65535
PORT = 9312


class ClientSocket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, addr):
        self.socket.connect((addr, PORT))

    def send_text(self, text):
        encoded_text = text.encode('utf-8')
        msg = Message(encoded_text)
        self.socket.sendall(msg.to_bytes())

        
sock = ClientSocket()
sock.connect("192.168.0.232")
while True:
    sock.send_text(input())