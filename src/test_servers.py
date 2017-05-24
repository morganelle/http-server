# -*- coding: utf-8 -*-
"""Test our Socket Echo assignment."""


import pytest


PARAMS_TABLE = [
    ("I Morgan"),
    ("abcdefghijklmnopqrstuveivmdnwjfidlwkfudjekweogutyfnfbvbcmdkedif"),
    ("Hi Kurt!"),
    (u'®'),
    ('1234.,.sadf'),
    ('.,.,.,.,.,.,.,.,.,.,.,.,.,')
]


"""messages shorter than one buffer in length"""
"""messages longer than several buffers in length"""
"""messages that are an exact multiple of one buffer in length"""
"""messages containing non-ascii characters"""


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
