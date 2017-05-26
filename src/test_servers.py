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


@pytest.mark.parametrize('request', PARAMS_TABLE)
def test_echo(request):
    """Test confirms client receives messages it sent to server."""
    from client import client
    assert client(request) == request
