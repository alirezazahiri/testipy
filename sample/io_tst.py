""" WRITE YOUR OWN CORRECT CODE TO TEST THE OUTPUT """

from math import factorial
from constants.settings import NUM_OF_TESTS


tests = [i for i in range(1, NUM_OF_TESTS+1)]

def main_code(test_index: int = 0):
    """ RETURN THE I/O THAT IS COMPATIBLE WITH YOUR TEST """

    i = f"{tests[test_index]}"  # some input
    o = f"{factorial(tests[test_index])}"  # some output

    return i, o
