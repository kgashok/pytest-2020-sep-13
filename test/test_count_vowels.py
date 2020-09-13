import pytest

from count_vowels import count_vowels


@pytest.mark.parametrize('s, count',  # part 1: a string with comma-separated variable names
                         [('', 0),  # part 2: a list of tuples; each tuple describes values assigned to the variables
                          ('rhythm', 0),
                          ('hello', 2),
                          ('GOODBYE', 3)])
def test_count_vowels(s, count):  # part 3: the variables are parameters for the function
    # part 4: we use the variables (parameters) in our test
    assert count_vowels(s) == count


def test_list():
    with pytest.raises(AttributeError):
        count_vowels(['abcdefg'])
