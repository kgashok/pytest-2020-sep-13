#!/usr/bin/env python3

def plword(s):
    s = s.lower()
    if s[0] in 'aeiou':
        return s + 'way'
    else:
        return s[1:] + s[0] + 'ay'


def 

# Pig Latin -- children's "secret" language

# - write a function that translates from English into Pig Latin
# - (assume all lowercase, one word, no punctuation)

# - write the function, plword
# - takes one argument (string)
# - returns one argument (string)

# rules:
# (1) If the word starts with a vowel, add "way"
# (2) Otherwise, move the first letter to the end, and add "ay"

# examples:
# - octopus -> octopusway
# - computer -> omputercay
# - table -> abletay
# - papaya -> apayapay

# the test for plword should:
# - handle empty string
# - handle words with vowels at the start
# - handle words with consonants at the start

# use parametrized tests to do this

# write a new function, print_plword, which prints the original word *and* the Pig Latin translation on the screen.
# use capsys to double check that the correct string was written.

# Example:

# print_plword('hello') should print 'hello is ellohay'
