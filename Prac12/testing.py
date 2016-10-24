"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac07.car import Car


def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    new = s
    for i in range(n-1):
        new += ' ' + s
    return new


def is_long_word(word, length=5):

    if len(word)>length:
        return True
    else:
        return False


def make_sentence(string):
    string.replace('.', '')
    string_list = list(string)
    string_list.append('.')
    string_list[0] = string_list[0].upper
    sentence = "".join(string_list)
    return sentence


def is_sentence(string):
    if make_sentence(string) == string:
        return True
    else:
        return False


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_word = 'python'
    assert is_long_word(test_word), "Word is not long enough"

    test_sentence = 'Hi my name is Hamish.'
    assert is_sentence(test_sentence), "Sentence incorrect format!"

    # TODO: 1. fix the repeat_string function above so that it passes the test
    # Hint: join

    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer != 0, "Car does not set odometer correctly"
    assert test_car.fuel != 0, "Car has no fuel"

    test_car = Car(fuel=10)
    assert test_car.fuel != 0, "Car has no fuel"
    # TODO: 2. write assert statements to show if Car sets the fuel correctly

run_tests()


# TODO: 3. Uncomment the following line and run the doctests
# doctest.testmod()

# TODO: 4. Fix the failing is_long_word function


# TODO: 5. Write and test a function to format a phrase as a sentence - starting with a capital and ending with a single full stop
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# "hello" -> "Hello."
# "It is an ex parrot." -> "It is an ex parrot."
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass