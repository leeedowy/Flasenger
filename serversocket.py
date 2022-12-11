import socket
from threading import Thread
from message import Message


DATA_BUFFER_SIZE = 4096
PORT = 9312


class ServerSocket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', PORT))

    def listen(self):
        self.socket.listen(5)
        while True:
            conn, addr = self.socket.accept()
            thread = Thread(target=self.handle_connection(conn, addr))
            thread.start()

    def handle_connection(self, conn, addr):
        with conn:
            print('Connected by', addr)
            header = bytes()
            while True:
                msg = None

                while len(header) < Message.HEADER_SIZE:
                    header += conn.recv(Message.HEADER_SIZE-len(header))
                    if not header: break

                payload_size = Message.extract_payload_size(header)
                payload = bytes()
                while header:
                    if len(payload) >= payload_size:
                        msg = Message(header=header, payload=payload[:payload_size])
                        next_payload = payload[payload_size:]
                        header = next_payload[:2]
                        payload = next_payload[2:]
                    else:
                        payload += conn.recv(DATA_BUFFER_SIZE)
                    if not payload: break

                if msg != None:
                    print(str(msg))
                if not payload and not msg: break
        print('Disconnected from', addr)

        
sock = ServerSocket()
sock.listen()