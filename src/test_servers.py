"""Test our Socket Echo assignment."""


import pytest


PARAMS_TABLE = [
    ("Hey Morgan"),
    ("abcdefghijklmnopqrstuveivmdnwjfidlwkfudjekweogutyfnfbvbcmdkedif"),
    ("Hi Kurt"),
    ('®')
]

@pytest.mark.parametrize('l', PARAMS_TABLE)
def test_echo(l):
    from client import client
    assert client(l) == l
"""messages shorter than one buffer in length"""
"""messages longer than several buffers in length"""
"""messages that are an exact multiple of one buffer in length"""
"""messages containing non-ascii characters"""
