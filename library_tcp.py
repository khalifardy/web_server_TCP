def balasan202(filename):
    header = "HTTP/1.0 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    files = open("html_file"+filename,'r')
    body = files.read()
    respon = header+content_type+body

    return respon

def balasan404():
    header = "HTTP/1.1 404 Not Found"
    content_type = "Content-Type: text/html\r\n\r\n"
    files = open("html_file/not_found.html",'r')
    body = files.read()
    respon = header+content_type+body

    return respon

def handle_client(client_socket):
    try:
        pesan = client_socket.recv(1024).decode()
        filename = pesan.split()[1]
        respon = balasan202(filename)
        client_socket.send(respon.encode())
        client_socket.close()
        
    except FileNotFoundError:
        respon = balasan404()
        client_socket.send(respon.encode())
        client_socket.close()
