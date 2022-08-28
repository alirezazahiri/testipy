""" WRITE YOUR OWN CORRECT CODE TO TEST THE OUTPUT """

from constants.settings import NUM_OF_TESTS
from math import *
import random

def check(a: int, b: int) -> bool:
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1

def main_code(test_index: int = 0):
    """ RETURN THE I/O THAT IS COMPATIBLE WITH YOUR TEST """
    n = random.randint(1, 1000)
    rand_num = random.randint(1, 1000000)
    i_list = []
    o_list = []
    for i in range(n):
        a = random.randint(1, 1000000)
        b = random.randint(a, 1000000)
        i_list.append(f"{a} {b}\n")
        o_list.append(f"{check(a, b)}\n")
    
    i = f"{n}\n{''.join(list(map(str, i_list)))}"  # some input
    o = f"{''.join(list(map(str, o_list)))}"  # some output

    return i, o
