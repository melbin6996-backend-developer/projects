import socket

HOST='127.0.0.1'
PORT= 8080

#create server socket
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connet socket to address + port
server.bind((HOST, PORT))

# Start listening
server.listen(5)

print(f"Server running on http://{HOST}:{PORT}")

while True:
    # wawit for browser connection
    client_socket, address = server.accept()

    print("Connected by:", address)

    # Recieve browser request
    request = client_socket.recv(1024).decode()

    print(request)

    # HTML webpage
    html = """
    <html>
        <body>
            <h1> Hello Melbin </h1>
            <p> You build your first raw web server !</p>
        </body>
    </html>
    """

    # HTTP response
    response = f"""
    HTTP/1.1 200 OK
    Content-Type: text.html
    {html}
    """
    # send response
    client_socket.send(response.encode())

    # Close connection
    client_socket.close()