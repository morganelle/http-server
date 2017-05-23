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

    try:
        while True:
            conn, addr = server.accept()
            client_message = b''
            buffer_length = 8
            complete = False

            while not complete:
                part = conn.recv(buffer_length)
                client_message += part
                print('in while, part:', part.decode('utf-8'))
                if client_message.decode('utf-8').endswith('.,.'):
                    complete = True

            print('server received: ', client_message)
            client_message = client_message
            conn.sendall(client_message)
            conn.close()

    except KeyboardInterrupt:
        conn.close()
        server.close()
        sys.exit()


if __name__ == '__main__':
    server()
