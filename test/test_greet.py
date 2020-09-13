from greet import greet


def test_greet(capsys):
    assert greet('world') == 'Hello, world!'
