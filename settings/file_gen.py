from sample.io_tst import main_code
from constants.COLORS import *
from constants.settings import IN_FILE_ROOT, NUM_OF_TESTS, OUT_FILE_ROOT


def generate(filename: str, rootPath: str = "", content: str = ""):
    """ GENERATES SOME FILES WITH CUSTOM EXTENSION IN SOME EXISTING DIRECTORY """
    with open(f"{rootPath}/{filename}", "w") as in_file:
        print(f"{content}", file=in_file, end="")
    in_file.close()


def create_files(count: int, extension: str):
    """ GENERATES THE I/O FILES FOR TEST PURPOSES """
    print(f"{OKBLUE}CREATING SAMPLES...{ENDC}")
    for i in range(count):
        content, result = main_code()
        generate(f"in-{i+1}.{extension}",
                 rootPath=IN_FILE_ROOT, content=content)
        generate(f"out-{i+1}.{extension}",
                 rootPath=OUT_FILE_ROOT, content=result)



def run():
    create_files(NUM_OF_TESTS, "txt")