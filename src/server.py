"""Server module for the Socket Echo assignment."""


import re
import socket
import sys
import os.path
import os
from datetime import datetime

LINE_BREAK = '\r\n'
CRLF = '\r\n\r\n'
ROOT_PATH = '../src/webroot'


def resolve_uri(uri):
    """Determine validity of resource request."""
    resource = uri.split()[-1][1:]
    request_path = os.path.join(ROOT_PATH, resource)
    print('request_path', request_path, 'isdir:', os.path.isdir(request_path))
    if os.path.isdir(request_path):
        print('Path match:', request_path)
        body = os.listdir(request_path)
        body = '<!DOCTYPE html><html><body><p>{}</p></body></html>'.format(body)
        size = len(body)
        return 'text/html', body, size
    elif os.path.isfile(request_path):
        print('File match:', request_path)
        file_type_dict = {
            'txt': 'text/plain',
            'html': 'text/html',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'ico': 'image/x-icon',
            'png': 'image/png',
            'mpeg': 'audio/mpeg',
            'ogg': 'audio/ogg',
            '*': 'audio/*',
            'mp4': 'video/mp4',
            'octet-stream': 'application/octet-stream'
        }
        split_request = request_path.split('.')
        file_type = file_type_dict[split_request[-1]]
        size = os.path.getsize(request_path)
        body = open(request_path, 'rb')
        body_read = body.read()
        body.close()
        return file_type, body_read, size
    else:
        raise ValueError('404')


def response_ok(uri):
    """Send an ok response."""
    content_type, content, size = resolve_uri(uri)
    response_ok = 'HTTP/1.1 200 OK\r\nContent-Type: {}\r\nContent-Length: {}{}{}{}'.format(
        content_type.encode('utf-8'),
        size,
        CRLF,
        content,
        CRLF)
    print(response_ok)
    return response_ok


def response_error(error):
    """Send an error response."""
    error_dict = {
        '404': 'HTTP/1.1 404 Not Found',
        '405': 'HTTP/1.1 405 Method Not Allowed',
        '505': 'HTTP/1.1 505 HTTP Version Not Supported'
    }
    print(error, error in error_dict)
    response_error = '{}{}'.format(
        error_dict.get(
            error, 'HTTP/1.1 400 Bad Request'), CRLF)
    print(error, 'response error before encoding', response_error)
    return response_error.encode('utf-8')


def parse_request(client_request):
    """Parse client HTTP request and raise errors."""
    get_present = re.compile(
        r'POST|PUT|HEAD|CONNECT|DELETE|OPTIONS|TRACE|PATCH')
    version_correct = re.compile(r'HTTP/1\.[^1]|HTTP/[^1]\.[^1]|HTTP/[^1]\.1')
    http_regex = re.compile(r'''(
        (GET\s)
        ([^\s]+\s)
        (HTTP/1\.1)
        (\r\n)
        (Host:\s)
        ([^\s]+)
        (.*)
        (\r\n\r\n)
        )''', re.VERBOSE | re.DOTALL)
    print(client_request)
    mo = http_regex.match(client_request)
    if mo is None:
        print('before if')
        if get_present.match(client_request) is not None:
            print('in 405 if')
            raise ValueError('405')
        elif version_correct.search(client_request) is not None:
            print('in 505 elif')
            raise ValueError('505')
        raise ValueError('400')
    uri = '{}{}'.format(mo.group(2), mo.group(3))
    print('uri', uri)
    return response_ok(uri)


def server():
    """Create socket and server."""
    server = socket.socket(family=socket.AF_INET,
                           type=socket.SOCK_STREAM,
                           proto=socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    print('server running at port', address[1])
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

            print('Server received: ', client_message.decode('utf-8'))
            try:
                conn.sendall(parse_request(client_message.decode('utf-8')))
                print("Message sent to client.\n")
            except ValueError as x:
                print('Except statement x:', x)
                conn.sendall(response_error(x[0]))
            conn.close()

    except KeyboardInterrupt:
        server.shutdown(socket.SHUT_WR)
        server.close()
        print('Exit complete.')
        sys.exit()


if __name__ == '__main__':
    server()
