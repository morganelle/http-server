# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


# import pytest


CRLF = '\r\n'
SUCCESS = b'HTTP/1.1 200 OK\r\n\r\n'


def test_uri_good():
    """."""
    from client import client
    assert client('GET / HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 135\r\n\r\n<!DOCTYPE html><html><body><p>[\'.DS_Store\', \'a_web_page.html\', \'favicon.ico\', \'images\', \'make_time.py\', \'sample.txt\']</p></body></html>\r\n\r\n'
