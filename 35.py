import socket

def send_request(host, port, request_file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        with open(request_file, 'r') as file:
            for line in file:
                sock.sendall(line.encode())
                response = sock.recv(1024).decode()
                print(response)
