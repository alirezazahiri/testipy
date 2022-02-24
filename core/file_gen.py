from sample.io_tst import main_code
from constants.COLORS import *
from constants.settings import IN_FILE_ROOT, NUM_OF_TESTS, OUT_FILE_ROOT

io_list = []


def generate(filename: str, rootPath: str = "", content: str = ""):
    """ GENERATES SOME FILES WITH CUSTOM EXTENSION IN SOME EXISTING DIRECTORY """
    with open(f"{rootPath}/{filename}", "w") as in_file:
        print(f"{content}", file=in_file, end="")
    in_file.close()


def create_files(count: int, extension: str):
    """ GENERATES THE I/O FILES FOR TEST PURPOSES """
    if len(io_list) != NUM_OF_TESTS:
        print(f"{OKBLUE}CREATING SAMPLES...{ENDC}")
    else:
        print(f"{OKBLUE}FETCHING SAMPLES...{ENDC}")
        
    for i in range(count):
        content, result = None, None
        if len(io_list) < count:
            content, result = main_code(i)
            if content.strip() == "":
                print(f"{FAIL}SAMPLE IS EMPTY...{ENDC}")
                print(f"{FAIL}EXITING...{ENDC}")
                exit(0)
            io_list.append((content, result))
        else:
            content, result = io_list[i]
        generate(f"in-{i+1}.{extension}",
                 rootPath=IN_FILE_ROOT, content=content)
        generate(f"out-{i+1}.{extension}",
                 rootPath=OUT_FILE_ROOT, content=result)


def run_file_gen():
    create_files(NUM_OF_TESTS, "txt")
