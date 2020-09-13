from pig import plword
import pytest

@pytest.mark.parametrize('eword, plword', 
    [("octopus", "octopusway") 
    ,("computer", "omputercay"), 
     ("table", "abletay"), 
     ("papaya", "apayapay")])
def test_words():
    assert plword(eword) == plword