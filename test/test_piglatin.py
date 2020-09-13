import pytest

from piglatin import plword


@pytest.mark.parametrize('one_word, translation',
                         [('cat', 'atcay'),
                          ('computer', 'omputercay'),
                          ('ELEPHANT', 'elephantway'),
                          ('octopus', 'octopusway')])
def test_plword(one_word, translation):
    assert plword(one_word) == translation
