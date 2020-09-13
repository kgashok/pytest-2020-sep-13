from greet import greet


def test_greet(capsys):
    greet('world')
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip() == 'Hello, world!'
