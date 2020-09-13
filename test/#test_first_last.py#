import pytest
from first_last import firstlast


@pytest.fixture
def simple_string():
    return 'abcd'


def test_simple(simple_string):
    assert firstlast(simple_string) == 'ad'


def test_element_0(simple_string):
    assert firstlast(simple_string)[0] == 'a'
