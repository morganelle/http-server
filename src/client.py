"""Client module for the Socket Echo assignment."""


import socket
import sys


def client(message):
    """Set up our client-side socket."""
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream[:3])
    client.connect(stream[-1])
    CRLF = '\r\n\r\n'
    client.sendall(message.encode('utf-8'))

    buffer_length = 256
    echo_message = b''

    complete = False
    while not complete:
        part = client.recv(buffer_length)
        echo_message += part
        if echo_message.decode('utf-8').endswith(CRLF):
            complete = True

    client.shutdown(socket.SHUT_WR)
    client.close()
    return echo_message.decode('utf-8')


if __name__ == '__main__':  # pragma no cover
    message = sys.argv[1]
    print(client(message))
    sys.exit()
