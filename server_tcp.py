from socket import socket,AF_INET,SOCK_STREAM,gethostname,SOL_SOCKET, SO_REUSEADDR
from library_tcp import handle_client
import sys
import threading


serverName = '127.0.0.1'
serverPort = 8000

try:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen()

    print("Server started on port %d" % serverPort)

    while True:
        koneksi, addr = serverSocket.accept()
        client_thread = threading.Thread(target=handle_client, 
                                         args=(koneksi,))
        client_thread.start()
        
    serverSocket.close()
    sys.exit()
except Exception as e:
    print(e)




