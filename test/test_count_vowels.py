import pytest

from count_vowels import count_vowels


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
        assert count_vowels(['abcdefg'])
