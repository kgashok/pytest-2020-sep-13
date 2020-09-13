import pytest

from count_vowels import count_vowels


@pytest.mark.parametrize('s, count',
                         [('', 0),
                          ('rhythm', 0),
                          ('hello', 2),
                          ('GOODBYE', 3)])
def test_count_vowels(s, count):
    assert count_vowels(s) == count


def test_list():
    with pytest.raises(AttributeError):
        count_vowels(['abcdefg'])
