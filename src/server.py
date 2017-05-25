"""Server module for the Socket Echo assignment."""


import re
import socket
import sys


CRLF = '\r\n\r\n'





def response_ok():
    """Send an ok response."""
    response_ok = 'HTTP/1.1 200 OK{}'.format(CRLF)
    return response_ok.encode('utf-8')


def response_error():
    """Send an error response."""
    response_error = 'HTTP/1.1 500 Internal Server Error{}'.format(CRLF)
    return response_error.encode('utf-8')


def parse_request(client_request):
    """Parse client HTTP request and raise errors."""
    http_regex = re.compile(r'''(
        (GET\s)
        ([^\s]+\s)
        (HTTP/1.1)
        (\r\n)
        (Host:\s)
        ([^\s]+)
        (\r\n\r\n)
        )''', re.VERBOSE)
    mo = http_regex.search(client_request)
    if mo is None:
        raise ConnectionRefusedError('Invalid HTTP request.')
    return response_ok()



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
            buffer_length = 256
            complete = False

            while not complete:
                part = conn.recv(buffer_length)
                client_message += part
                if client_message.decode('utf-8').endswith(CRLF):
                    complete = True

            print('server received: ', client_message.decode('utf-8'))
            try:
                conn.sendall(parse_request(client_message.decode('utf-8')))
            except ConnectionRefusedError:
                conn.sendall(response_error())
            conn.close()

    except KeyboardInterrupt:
        server.shutdown(socket.SHUT_WR)
        server.close()
        print('Exit complete.')
        sys.exit()


if __name__ == '__main__':
    server()
