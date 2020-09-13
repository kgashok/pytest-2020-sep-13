import pytest

from count_vowels import count_vowels


@pytest.mark.parametrize('s, count',
                         [('', 0),
                          ('rhythm', 0),
                          ('
def test_count_vowels():
    

def test_count_empty():
    assert count_vowels('') == 0


def test_no_vowel_word():
    assert count_vowels('rhythm') == 0


def test_simple_word():
    assert count_vowels('hello') == 2


def test_simple_goodbye():
    assert count_vowels('GOODBYE') == 3


def test_list():
    with pytest.raises(AttributeError):
        count_vowels(['abcdefg'])
