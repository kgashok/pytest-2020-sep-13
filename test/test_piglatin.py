import pytest
from io import StringIO

from piglatin import plword, print_plword, print_interactive_plword


@pytest.mark.parametrize('one_word, translation',
                         [('cat', 'atcay'),
                          ('computer', 'omputercay'),
                          ('ELEPHANT', 'elephantway'),
                          ('octopus', 'octopusway')])
def test_plword(one_word, translation):
    assert plword(one_word) == translation


@pytest.mark.parametrize('one_word, translation',
                         [('cat', 'atcay'),
                          ('computer', 'omputercay'),
                          ('ELEPHANT', 'elephantway'),
                          ('octopus', 'octopusway')])
def test_print_plword(capsys, one_word, translation):
    print_plword(one_word)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip() == f'{one_word} is {translation}'


def test_print_interactive_plword(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('hello'))
    print_interactive_plword()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip() == f'hello is ellohay'
