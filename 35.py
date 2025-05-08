import socket

def send_request(host, port, request_file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        with open(request_file, 'r') as file:
            for line in file:
                sock.sendall(line.encode())
                response = sock.recv(1024).decode()
                print(response)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python client.py <hostname> <port> <request_file>")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        request_file = sys.argv[3]
        send_request(host, port, request_file)