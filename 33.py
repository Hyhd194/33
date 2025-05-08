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

    def process_request(self, request):
        parts = request.split()
        command = parts[0]
        key = parts[1]
        value = ' '.join(parts[2:])

        if command == "PUT":
            if key in self.tuple_space:
                return "010ERR key already exists"
            else:
                self.tuple_space[key] = value
                return f"010OK ({key}, {value}) added"
        elif command == "GET":
            if key in self.tuple_space:
                value = self.tuple_space.pop(key)
                return f"010OK ({key}, {value}) removed"
            else:
                return "010ERR key does not exist"
        elif command == "READ":
            if key in self.tuple_space:
                value = self.tuple_space[key]
                return f"010OK ({key}, {value}) read"
            else:
                return "010ERR key does not exist"
        else:
            return "007ERR Unknown command"
