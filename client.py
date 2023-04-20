import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])
path = sys.argv[3]

client_socket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM
                                )

client_socket.connect((host, port))

request = f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n"
client_socket.send(request.encode())

response = client_socket.recv(1024)
print(response.decode())

client_socket.close()