import socket

PORT = 6969

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []

    def connect(self, peer_host, peer_port):
        try:
            connection = self.socket.connect((peer_host, peer_port))
            self.connections.append(connection)
            print(f'Connected to {peer_host}L{peer_port}')
        except socket.error as e:
            print(f'Failed to connect to {peer_host}:{peer_port}')

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        print(f'Listening for connections on {self.host}:{self.port}')