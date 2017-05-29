# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


# import pytest


# CRLF = '\r\n'
# SUCCESS = b'HTTP/1.1 200 OK\r\n\r\n'


# def test_uri_good():
#     """."""
#     from client import client
#     assert client(
#         'GET /pickles HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == '\nHTTP/1.1 200 OK\nDate: Mon, 29 May 2017 09:49:41\nContent-Type: text/html\nContent-Length: 135\n\n<!DOCTYPE html><html><body><p>[\'images\', \'make_time.py\', \'a_web_page.html\', \'.DS_Store\', \'favicon.ico\', \'sample.txt\']</p></body></html>\r\n\r\n'


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
ROOT_LIST_RESP = SUCCESS
b'Date: Mon, 29 May 2017 09:49:41\r\n'
'Content-Type: text/html\r\n'
'Content-Length: 135\r\n\r\n'
'<!DOCTYPE html><html><body><p>'
'[\'.DS_Store\', '
'\'a_web_page.html\', '
'\'favicon.ico\', '
'\'images\','
' \'make_time.py\', '
'\'sample.txt\']</p></body></html>\r\n\r\n'
IMAGES_LIST_RESP = SUCCESS + b'Date: Mon, 29 May 2017 09:49:41\r\nContent-Type: text/html\r\nContent-Length: 110\r\n\r\n<!DOCTYPE html><html><body><p>[\'Sample_Scene_Balls.jpg\', \'JPEG_example.jpg\', \'sample_1.png\']</p></body></html>\r\n\r\n'
WEB_PAGE_RESP = SUCCESS + b'Date: Mon, 29 May 2017 09:49:41\r\nContent-Type: text/html\r\nContent-Length: 125\r\n\r\n'


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
