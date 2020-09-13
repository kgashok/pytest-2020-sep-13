from vowels import count_vowels
from string import ascii_lowercase as alphabets

def test_empty_string():
    assert count_vowels("") == 0

def test_alphabets():
    assert count_vowels(alphabets) == 5

