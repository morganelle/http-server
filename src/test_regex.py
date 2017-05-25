"""Test regex against headers."""


import pytest

PARAMS_TABLE = [

    ['FOOBARAL /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['POST /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GE /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GET/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GET HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GET/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GETHTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GET /path/file.html HTTP/1.1\r\nwww.host1.com:80\r\n\r\n', True],
    ['GET /path/file.html HTTP/1.1\r\n\r\n\r\n', True],
    ['GET /path/file.html HTTP/1.1Host: www.host1.com:80\r\n\r\n', True],
    ['GET /path/file.html\r\nHost: www.host1.com:80', True],
    ['GET\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GET /path/file.html HTTP/1.1\r\nHost: asdfafjasldkfjei\r\n\r\n', False],
    ['GET / HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', False],
    ['GET /path HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', False],
    ['GET /foobarfile.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', False],
    ['GET /somecrap HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', False],
    ['GET `~<>,.?/''""\{\}[]|\ HTTP/1.1\r\nHost: !@#$#$%^^&&**()_=-\r\n\r\n', False],
    ['GET garbage HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', False],
    ['GET /path/file.html HTTP/1.1\r\nHost: www0\r\n\r\n', False],
    ['GET /path/file.html    HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GET /path/file.htmlHTTP/1.1\r\nHost:www.host1.com:80\r\n\r\n', True],
    ['GET /path/file.htmlHTTP/1.1Host:www.host1.com:80', True],
    ['GET\r\n\r\n', True],
    ['/path/file.html', True],
    ['HTTP/1.1\r\n', True],
    ['Host: www.host1.com:80', True],
    ['GET /path/file.html HTTP/1.1\r\n\sHost: www.host1.com:80\r\n\r\\', True],
    ['GET /path/file.html HTTP/1.1\r\rHost: www.host1.com:80\r\n\r', True],
    ['GET    /path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n', True],
    ['GET/path/file.html HTTP/1.1\r\n\r\n\r\n\rHost: www.host1.com:80\r\n\r\n', True],
    ['', True]
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_regex(l, result):
    """Test the regex to parse headers."""
    from regex_exp import request_parser
    assert request_parser(l) == result
