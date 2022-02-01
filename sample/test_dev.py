from sample.io_tst import main_code


def test_main_code():
    i, o = main_code()

    print(f"inputs:\n{i}")
    print(f"outputs:\n{o}")
