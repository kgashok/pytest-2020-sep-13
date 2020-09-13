from mysum import mysum

def test_for_10_for_range_10():

    alist = list(range(10))
    assert mysum(alist) == 45

def test_for_0_for_range_0():
    alist = []
    assert mysum(alist) == 0

