#!/usr/bin/env python3

def count_vowels(s: str) -> int:
    total = 0

    for one_letter in s.lower():
        if one_letter in 'aeiou':
            total += 1

    return total

# write a function, count_vowels, which takes a string as
# an argument and returns an integer count of how many
# vowels were in the string

# - create the file/function
# - create the test file
# - write a bunch of tests
#   - empty string?
#   - no vowels?


if __name__ == '__main__':
    print(count_vowels('abcde'))
