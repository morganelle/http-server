# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


import pytest


CRLF = '\r\n'
SUCCESS = 'HTTP/1.1 200 OK{}{}'.format(CRLF * 2)


PARAMS_TABLE = [
    ("I Morgan"),
    ("abcdefghijklmnopqrstuveivmdnwjfidlwkfudjekweogutyfnfbvbcmdkedif"),
    ("Hi Kurt!"),
    (u'®'),
    ('1234.,.sadf'),
    ('.,.,.,.,.,.,.,.,.,.,.,.,.,')
]

HTTP_REQUEST_PARAMS = [
    ['GET / HTTP/1.1{}host: www.example.com{}'.format(CRLF, CRLF * 2), SUCCESS]
]


# @pytest.mark.parametrize('l', PARAMS_TABLE)
# def test_echo(l):
#     """Test confirms client receives messages it sent to server."""
#     from client import client
#     assert client(l) == l


@pytest.mark.parametrize('l', PARAMS_TABLE)
def test_response_ok(l):
    """Test confirms client receives status message."""
    from client import client
    assert client(l) == 'HTTP/1.1 200 OK\r\n\r\n'


# test for multiple values passed in


@pytest.mark.parametrize('request, response', HTTP_REQUEST_PARAMS)
def test_parse_request_method_success(request, response):
    """Test for request type."""
    from client import client
    assert client(request) == response


# def test_parse_request_method_fail():
#     """Test for request type"""
#     from client import client
#     with pytest.raises(ConnectionRefusedError):
#         parse_request(INSERT VALUE!!)
