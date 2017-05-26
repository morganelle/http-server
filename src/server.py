"""Server module for the Socket Echo assignment."""


import re
import socket
import sys


CRLF = '\r\n\r\n'


def response_ok():
    """Send an ok response."""
    response_ok = 'HTTP/1.1 200 OK{}'.format(CRLF)
    return response_ok.encode('utf-8')


def response_error(error):
    """Send an error response."""
    error_dict = {
        '405': '405 Method Not Allowed',
        '505': '505 HTTP Version Not Supported'
    }
    response_error = '{}{}'.format(error_dict.get(error, '400 Not Found'), CRLF)  # default needs editing
    print('response error before encoding', response_error)
    return response_error.encode('utf-8')


def parse_request(client_request):
    """Parse client HTTP request and raise errors."""
    get_present = re.compile(r'POST|PUT|HEAD|CONNECT|DELETE|OPTIONS|TRACE|PATCH')
    version_correct = re.compile(r'HTTP/1.1')
    http_regex = re.compile(r'''(
        (GET\s)
        ([^\s]+\s)
        (HTTP/1.1)
        (\r\n)
        (Host:\s)
        ([^\s]+)
        (\r\n\r\n)
        )''', re.VERBOSE)
    mo = http_regex.match(client_request)
    if mo is None:
        print('before if')
        if get_present.match(client_request) is not None:
            print('in if')
            raise ValueError('405')
        elif version_correct.match(client_request) is None:
            print('in elif')
            raise ValueError('505')
        raise ValueError()
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
            except ValueError as x:
                conn.sendall(response_error(x))
            conn.close()

    except KeyboardInterrupt:
        server.shutdown(socket.SHUT_WR)
        server.close()
        print('Exit complete.')
        sys.exit()


if __name__ == '__main__':
    server()
