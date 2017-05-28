# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


# import pytest


CRLF = '\r\n'
SUCCESS = b'HTTP/1.1 200 OK\r\n\r\n'


def test_uri_good():
    """."""
    from client import client
    assert client('GET / HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 272\r\n<p>[\'.DS_Store\', \'a_web_page.html\', \'favicon.ico\', \'images\', \'make_time.py\', \'sample.txt\']</p>\r\n\r\n'


# def test_path_good():
#     """."""
#     from client import client
#     assert client('GET /webroot HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == b'HTTP/1.1 200 OK\r\nGET /path/file.html \r\n\r\n'


# def test_file_good():
#     """."""
#     from client import client
#     assert client('GET /webroot/images/JPEG_example.jpg HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == b'HTTP/1.1 200 OK\r\nGET /path/file.html \r\n\r\n'


# def test_uri_bad():
#     """."""
#     from client import client
#     assert client('GET / HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n') == b'HTTP/1.1 404 Not Found\r\n\r\n'
