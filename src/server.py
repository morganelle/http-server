"""Server module for the Socket Echo assignment."""


import socket
import sys


def server():
    """Create socket and server."""
    server = socket.socket(family=socket.AF_INET,
                           type=socket.SOCK_STREAM,
                           proto=socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()

    client_message = ''
    buffer_length = 8
    complete = False

    while not complete:
        part = conn.recv(buffer_length)
        client_message += part.decode('utf8')
        if len(part) < buffer_length:
            complete = True

    print('server received: ', client_message)
    client_message = client_message.encode('utf8')
    conn.sendall(client_message)
    conn.close()

if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        sys.exit()
