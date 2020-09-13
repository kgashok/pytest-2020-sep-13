from mysum import mysum


def test_mysum_simple():
    assert mysum([10, 20, 30]) == 60
    assert mysum([10.5, 20, 30]) == 60.5
