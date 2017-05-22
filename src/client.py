"""Module for the Socket Echo assignment."""


import socket
import sys


def client(message):
    """Set up our client-side socket."""
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream = [i for i in info if i[1] == socket.SOCK_STREAM[0]]
    client = socket.socket(*stream[:3])
    client.connect(stream[-1])

    client.sendall(message.encode('utf-8'))

    buffer_length = 8
    echo_message = ""

    # while part != 0:
    #     part = client.recv(buffer_length)
    #     echo_message += part

    # return echo_message

    complete = False
    while not complete:
        part = client.recv(buffer_length)
        echo_message += part
        if len(part) < buffer_length:
            complete = True


if __name__ == '__main__':
    while True:
        client(message)
        try:
            exit = input("Press [Ctrl+D] to quit.")
        except EOFError:
            client.close()
            sys.exit()
