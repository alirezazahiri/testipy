""" WRITE YOUR OWN CORRECT CODE TO TEST THE OUTPUT """

import random

def to_str(num: int):
    return f"{num}\n"

def is_prime(num: int):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False 
    for i in range(3, num // 2):
        if num % i == 0:
            return False
    return True

def main_code(): 
    """ RETURN THE I/O THAT IS COMPATIBLE WITH YOUR TEST """
    n = random.randint(1, 1000)
    nums = [random.randint(0, 999999) for _ in range(n)]
    primes = [num for num in nums if is_prime(num)]

    i = f"{n}\n{' '.join(list(map(str, nums)))}"
    o = f"{''.join(list(map(to_str, primes)))}"

    return i, o