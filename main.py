from clientsocket import ClientSocket


if __name__ == '__main__':
    socket = ClientSocket()
    socket.connect("192.168.0.232")

    HOST = '192.168.0.232'    # The remote host
    PORT = 50007              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while (True):
            payload = input()
            if (payload == "exit"):
                break
            s.sendall(payload.encode('utf-8'))

# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9312               # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            print(data)