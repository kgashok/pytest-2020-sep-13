#!/usr/bin/env python3

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def greet(self):
        return f'Hello, {self.fullname()}!'

    def __repr__(self):
        return f'Person, vars = {vars(self)}'


# create a Person class in person.py

# the class should have attributes:
# - first_name
# - last_name
# - age

# it should have methods:
# - fullname (combine first and last)
# - greet (returns a "Hello" string to them)
# - __repr__ -- should return a string with all three attribute names + values (you can use "vars" for this)

# Have your tests:
# - check (with the pytest.raises assertion) that we are creating a valid object with the right number of arguments
# - when we call the methods, we should get appropriate values back
# - use parametrization to reduce code writing
