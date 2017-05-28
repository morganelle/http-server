# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


# import pytest


CRLF = '\r\n'
SUCCESS = b'HTTP/1.1 200 OK\r\n\r\n'


# HTTP_REQUEST_PARAMS_OK = [
#     ['GET /path/file.html HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET /path/file.html \r\n\r\n'],
#     ['GET / HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET / \r\n\r\n'],
    # ['GET /path HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET /path \r\n\r\n'],
    # ['GET /foobarfile.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET /foobarfile.html \r\n\r\n'],
    # ['GET /somecrap HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET /somecrap \r\n\r\n'],
    # ['GET `~<>,.?/''""\{\}[]|\ HTTP/1.1\r\nHost: !@#$#$%^^&&**()_=-\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET `~<>,.?/""\{\}[]|\ \r\n\r\n'],
    # ['GET garbage HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET garbage \r\n\r\n'],
    # ['GET /path/file.html HTTP/1.1\r\nHost: www0\r\n\r\n', b'HTTP/1.1 200 OK\r\nGET /path/file.html \r\n\r\n'],
# ]


# def test_uri_good():
    # """."""
    # from client import client
    # assert client('GET /path/file.html HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == b'HTTP/1.1 200 OK\r\nGET /path/file.html \r\n\r\n'


def test_path_good():
    """."""
    from client import client
    assert client('GET /webroot HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n') == b'HTTP/1.1 200 OK\r\nGET /path/file.html \r\n\r\n'


# def test_uri_bad():
#     """."""
#     from client import client
#     assert client('GET / HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n') == b'HTTP/1.1 404 Not Found\r\n\r\n'


# HTTP_REQUEST_PARAMS_EXCEPT = [
#     'PUT /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET /path/file.html HTTP/1.0\r\nHost: www.host1.com:80\r\n\r\n',
#     'POST /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GE /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     '/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GETHTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET /path/file.html HTTP/1.1\r\nwww.host1.com:80\r\n\r\n',
#     'GET /path/file.html HTTP/1.1\r\n\r\n\r\n',
#     'GET /path/file.html HTTP/1.1Host: www.host1.com:80\r\n\r\n',
#     'GET /path/file.html\r\nHost: www.host1.com:80',
#     'GET\r\nHost: www.host1.com:80\r\n\r\n',
#     'get garbage HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET /path/file.html    HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET /path/file.htmlHTTP/1.1\r\nHost:www.host1.com:80\r\n\r\n',
#     'GET /path/file.htmlHTTP/1.1Host:www.host1.com:80',
#     'GET\r\n\r\n',
#     '/path/file.html',
#     'HTTP/1.1\r\n',
#     'Host: www.host1.com:80',
#     'GET /path/file.html HTTP/1.1\r\n\sHost: www.host1.com:80\r\n\r\\',
#     'GET /path/file.html HTTP/1.1\r\rHost: www.host1.com:80\r\n\r',
#     'GET    /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n',
#     'GET/path/file.html HTTP/1.1\r\n\r\n\r\n\rHost: www.host1.com:80\r\n\r\n',
#     ''
# ]


# # @pytest.mark.parametrize('request, result', HTTP_REQUEST_PARAMS_OK)
# def test_response_ok():
#     """Test confirms client receives status message."""
#     from client import client
#     assert client('GET /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n') == 'HTTP/1.1 200 OK\r\nGET /path/file.html \r\n\r\n'


# # @pytest.mark.parametrize('request, result', HTTP_REQUEST_PARAMS_OK)
# def test_response_405():
#     """Test confirms client receives status message."""
#     from client import client
#     assert client('PUT /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n') == 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'


# # @pytest.mark.parametrize('request, result', HTTP_REQUEST_PARAMS_OK)
# def test_response_505():
#     """Test confirms client receives status message."""
#     from client import client
#     assert client('GET /path/file.html HTTP/1.0\r\nHost: www.host1.com:80\r\n\r\n') == 'HTTP/1.1 505 HTTP Version Not Supported\r\n\r\n'


# @pytest.mark.parametrize('l, result', HTTP_REQUEST_PARAMS_OK)
# def test_regex_ok(l, result):
#     """Test the regex to parse headers."""
#     from server import parse_request
#     assert parse_request(l) == result


# @pytest.mark.parametrize('l', HTTP_REQUEST_PARAMS_EXCEPT)
# def test_regex_except(l):
#     """Test the regex to parse headers."""
#     from server import parse_request
#     with pytest.raises(ValueError):
#         parse_request(l)
