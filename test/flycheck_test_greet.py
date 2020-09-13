from pytest import capsys
from greet import greet


def test_greet():
    assert greet('world') == 'Hello, world!'
