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

    def handle_client(self, client_socket):
        while True:
            try:
                request = client_socket.recv(1024).decode()
                if not request:
                    break
                response = self.process_request(request)
                client_socket.send(response.encode())
            except Exception as e:
                print(f"Error handling client: {e}")
                break
        client_socket.close()
