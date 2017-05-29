# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


# import pytest


CRLF = '\r\n'
SUCCESS = b'HTTP/1.1 200 OK\r\n'
WEB_PAGE_CONTENT = '''<!DOCTYPE html>
<html>
<body>

<h1>Code Fellows</h1>

<p>A fine place to learn Python web programming!</p>

</body>
</html>'''
ROOT_LIST_RESP = SUCCESS + b'Content-Type: text/html\r\nContent-Length: 135\r\n\r\n<!DOCTYPE html><html><body><p>[\'.DS_Store\', \'a_web_page.html\', \'favicon.ico\', \'images\', \'make_time.py\', \'sample.txt\']</p></body></html>\r\n\r\n'
IMAGES_LIST_RESP = SUCCESS + b'Content-Type: text/html\r\nContent-Length: 110\r\n\r\n<!DOCTYPE html><html><body><p>[\'JPEG_example.jpg\', \'sample_1.png\', \'Sample_Scene_Balls.jpg\']</p></body></html>\r\n\r\n'
WEB_PAGE_RESP = SUCCESS + b'Content-Type: text/html\r\nContent-Length: 125\r\n\r\n'


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
