# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


import pytest


CRLF = '\r\n'
SUCCESS = b'HTTP/1.1 200 OK\r\n'
ROOT_LIST_RESP = SUCCESS + b'Content-Type: text/html\r\nContent-Length: 135\r\n\r\n<!DOCTYPE html><html><body><p>[\'.DS_Store\', \'a_web_page.html\', \'favicon.ico\', \'images\', \'make_time.py\', \'sample.txt\']</p></body></html>\r\n\r\n'
IMAGES_LIST_RESP = SUCCESS + b'Content-Type: text/html\r\nContent-Length: 110\r\n\r\n<!DOCTYPE html><html><body><p>[\'JPEG_example.jpg\', \'sample_1.png\', \'Sample_Scene_Balls.jpg\']</p></body></html>\r\n\r\n'
WEB_PAGE_RESP = SUCCESS + b'Content-Type: text/html\r\nContent-Length: 125\r\n\r\n'

RESPONSE_400 = b'HTTP/1.1 400 Bad Request\r\n\r\n'
RESPONSE_404 = b'HTTP/1.1 404 Not Found\r\n\r\n'
RESPONSE_405 = b'HTTP/1.1 405 Method Not Allowed\r\n\r\n'
RESPONSE_505 = b'HTTP/1.1 505 HTTP Version Not Supported\r\n\r\n'

HTTP_REQUEST_PARAMS_400 = [
    # ('PUT /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', RESPONSE_404),
    # ('GET /path/file.html HTTP/1.0\r\nHost: www.host1.com:80\r\n\r\n', RESPONSE_505),
    # ('POST /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', RESPONSE_505),
    'GE /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
    'GET/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
    '/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
    # ('GET HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'),
    # ('GET/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'),
    # ('GETHTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'),
    # ('GET /path/file.html HTTP/1.1\r\nwww.host1.com:80\r\n\r\n'),
    # ('GET /path/file.html HTTP/1.1\r\n\r\n\r\n'),
    # ('GET /path/file.html HTTP/1.1Host: www.host1.com:80\r\n\r\n'),
    # ('GET /path/file.html\r\nHost: www.host1.com:80'),
    # ('GET\r\nHost: www.host1.com:80\r\n\r\n'),
    # ('get garbage HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'),
    # ('GET /path/file.html    HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'),
    # ('GET /path/file.htmlHTTP/1.1\r\nHost:www.host1.com:80\r\n\r\n'),
    # ('GET /path/file.htmlHTTP/1.1Host:www.host1.com:80'),
    'GET\r\n\r\n',
    '/path/file.html\r\n\r\n'
    # ('HTTP/1.1\r\n'),
    # ('Host: www.host1.com:80'),
    # ('GET /path/file.html HTTP/1.1\r\n\sHost: www.host1.com:80\r\n\r\\'),
    # ('GET /path/file.html HTTP/1.1\r\rHost: www.host1.com:80\r\n\r'),
    # ('GET    /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'),
    # ('GET/path/file.html HTTP/1.1\r\n\r\n\r\n\rHost: www.host1.com:80\r\n\r\n'),
    # ('')
]

HTTP_REQUEST_PARAMS_405 = [
    'PUT /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
    'POST /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'
]


def test_uri_good_root_dir():
    """."""
    from client import client
    assert client('GET / HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == ROOT_LIST_RESP


def test_uri_good_images_dir():
    """."""
    from client import client
    assert client('GET /images HTTP/1.1\r\nHost: www.example.com\r\n\r\n') == IMAGES_LIST_RESP


def test_uri_good_html():
    """."""
    from client import client
    assert client('GET /a_web_page.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n').startswith(WEB_PAGE_RESP)


@pytest.mark.parametrize('request', HTTP_REQUEST_PARAMS_400)
def test_exceptions_400(request):
    """."""
    from client import client
    assert client(request) == RESPONSE_400


@pytest.mark.parametrize('request', HTTP_REQUEST_PARAMS_405)
def test_exceptions_405(request):
    """."""
    from client import client
    assert client(request) == RESPONSE_405
