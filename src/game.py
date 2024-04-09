from connHandler import ConnHandler
import socket

class Game:
    def __init__(self) -> None:
        self.connection_handler = ConnHandler()
        self.test()
        
    def test(self):
        mode = input('Mode: ')
        if mode == 'c':
            # TEST
            self.connection_handler.connect(socket.gethostname())
        else:
            self.connection_handler.listen()

if __name__ == '__main__':
    Game()