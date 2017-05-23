"""Client module for the Socket Echo assignment."""


import socket
import sys


def client(message):
    """Set up our client-side socket."""
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream[:3])
    client.connect(stream[-1])
    message += '.,.'
    client.sendall(message.encode('utf-8'))
    print('I sent the client', message)

    buffer_length = 8
    echo_message = ""
    print(echo_message)

    complete = False
    while not complete:
        part = client.recv(buffer_length)
        echo_message += part.decode('utf-8')
        print(part)
        if echo_message.endswith('.,.'):
            print('True')
            complete = True

    client.shutdown(socket.SHUT_WR)
    client.close()
    return echo_message[:-3]


if __name__ == '__main__':
    message = sys.argv[1]

    print(client(message))
    sys.exit()
