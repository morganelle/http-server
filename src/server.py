"""Server module for the Socket Echo assignment."""


import re
import socket
import sys


LINE_BREAK = '\r\n'
CRLF = '\r\n\r\n'


def response_ok(uri):
    """Send an ok response."""
    response_ok = 'HTTP/1.1 200 OK{}{}{}'.format(LINE_BREAK, uri, CRLF)
    return response_ok.encode('utf-8')


def response_error(error):
    """Send an error response."""
    error_dict = {
        '405': 'HTTP/1.1 405 Method Not Allowed',
        '505': 'HTTP/1.1 505 HTTP Version Not Supported'
    }
    response_error = '{}{}'.format(
        error_dict.get(error, '400 Not Found'), CRLF)
    return response_error.encode('utf-8')


def parse_request(client_request):
    """Parse client HTTP request and raise errors."""
    get_present = re.compile(
        r'POST|PUT|HEAD|CONNECT|DELETE|OPTIONS|TRACE|PATCH')
    version_correct = re.compile(r'HTTP/[^1]\.1|HTTP/[^1]\.[^1]|HTTP/1\.[^1]')
    http_regex = re.compile(r'''(
        (GET\s)
        ([^\s]+\s)
        (HTTP/1\.1)
        (\r\n)
        (Host:\s)
        ([^\s]+)
        (\r\n\r\n)
        )''', re.VERBOSE)
    mo = http_regex.match(client_request)
    if mo is None:
        if get_present.match(client_request) is not None:
            raise ValueError('405')
        elif version_correct.match(client_request) is not None:
            raise ValueError('505', '404')
        raise ValueError()
    uri = '{}{}'.format(mo.group(2), mo.group(3))
    return response_ok(uri)


def server():
    """Create socket and server."""
    server = socket.socket(family=socket.AF_INET,
                           type=socket.SOCK_STREAM,
                           proto=socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    print('Server running on port 5000')

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
            try:
                conn.sendall(parse_request(client_message.decode('utf-8')))
            except ValueError as x:
                conn.sendall(response_error(x[0]))
            conn.close()

    except KeyboardInterrupt:
        server.shutdown(socket.SHUT_WR)
        server.close()
        print('Exit complete.')
        sys.exit()


if __name__ == '__main__':
    server()
