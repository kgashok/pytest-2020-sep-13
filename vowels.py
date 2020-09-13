# write a function, count_vowels, which takes a string as
# an argument and returns an integer count of how many
# vowels were in the string

# - create the file/function
# - create the test file
# - write a bunch of tests
#   - empty string?
#   - no vowels?

def count_vowels(seq):
    vowels = "aeiou"
    count = 0
    for t in seq:
        if t in vowels:
            count += 1
    return count
    