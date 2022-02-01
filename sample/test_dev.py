from constants.COLORS import *
from sample.io_tst import main_code


def test_main_code():
    print(f"{OKCYAN}")
    i, o = main_code()
    print(f"{ENDC}")

    print(f"inputs:\n{i}")
    print(f"outputs:\n{o}")
