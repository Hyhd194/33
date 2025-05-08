import socket
import threading

class TupleSpaceServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.tuple_space = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
