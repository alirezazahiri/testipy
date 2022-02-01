""" WRITE YOUR OWN CORRECT CODE TO TEST THE OUTPUT """

import random
from constants.settings import NUM_OF_TESTS


def main_code(test_index: int = 0):
    """ RETURN THE I/O THAT IS COMPATIBLE WITH YOUR TEST """
    n = random.randint(1, 1000)
    arr = [random.randint(1, 100000) for _ in range(n)]
    
    i = f"{n}\n{' '.join(list(map(str, arr)))}"  # some input
    o = f"{max(arr)}\n"  # some output

    return i, o
