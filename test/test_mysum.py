import pytest
from mysum import mysum
import random
import os


# create a fixture, random_numbers,
# which returns a tuple of 2 elements
# - a list of random numbers
# - the sum of those random numbers

# (1) try this with a regular fixture, and see
#  that the numbers change each time.

# (2) then set the random seed to 0
#  each time the fixture runs, and see that
#  you get the same values each time

# (3) then get rid of the random.seed, but
#  set the fixture's scope to be "module"
#  and you should still get the same values each time
#  @pytest.fixture(scope='module')

def test_mysum_simple():
    assert mysum([10, 20, 30]) == 60
    assert mysum([10.5, 20, 30]) == 60.5


@pytest.mark.negative
def test_mysum_neg():
    assert mysum([-5, -10, -15]) == -30


@pytest.mark.nonint
def test_mysum_float():
    assert mysum([10.5, 20.5, 30.5]) == 61.5


@pytest.mark.nonint
@pytest.mark.negative
def test_mysum_float2():
    assert mysum([10.5, -20.5, 30.5]) == 20.5


def test_mysum_bad_floats():
    assert pytest.approx(mysum([0.1, 0.2])) == 0.3


@pytest.fixture(scope='module')
def standard_numbers():
    numbers = [random.randint(0, 100) for i in range(5)]
    return numbers, sum(numbers)


def test_standard_numbers1(standard_numbers):
    numbers, total = standard_numbers
    print(f'{numbers=}, {total=}')
    assert mysum(numbers) == total


def test_standard_numbers2(standard_numbers):
    numbers, total = standard_numbers
    print(f'{numbers=}, {total=}')
    assert mysum(numbers) == total


@pytest.fixture
def standard_numbers_with_file():
    numbers = [random.randint(0, 100) for i in range(5)]
    with open('/tmp/mydata.txt', 'a') as f:
        f.write(f'{numbers=}\n')

    # above this line runs *before* the test function is called

    yield numbers, sum(numbers)

    # under this line runs *after* the test function is done
    os.unlink('/tmp/mydata.txt')


def test_standard_numbers_file1(standard_numbers_with_file):
    numbers, total = standard_numbers_with_file
    print(f'{numbers=}, {total=}')
    assert mysum(numbers) == total


def test_standard_numbers_file2(standard_numbers_with_file):
    numbers, total = standard_numbers_with_file
    print(f'{numbers=}, {total=}')
    assert mysum(numbers) == total
