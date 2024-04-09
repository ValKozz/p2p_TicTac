from peer import Peer
import socket

class ConnHandler:
    def __init__(self):
        # port = self.handleAddr()
        self.defaultOutPort = 6969
        self.peer = Peer(socket.gethostname(), port=self.defaultOutPort)


    
    def handleAddr(self):
        port = False
        while not port:
            try:
                port = int(input('Input port to play on: '))
            except Exception as e:
                print(f'Please enter the appropriate port! ({e})')
        return port

    def listen(self):
        self.peer.start()

    def connect(self, ip_addr):
        self.peer.connect(ip_addr, self.defaultOutPort)
