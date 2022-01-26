import subprocess as sb
import os
import shutil
from settings.file_gen import run
from constants.COLORS import *
from constants.settings import IN_FILE_ROOT, NUM_OF_TESTS, OUT_FILE_ROOT, RESULT_FILE_ROOT, TEST_ROOT, TARGET_ROOT


def finish():
    """ REMOVE ALL TEST FILES CREATED """
    try:
        shutil.rmtree(f"{TEST_ROOT}")
    except:
        return


def execute(FILE: str):
    """ RUN ANY .cpp FILE INSIDE THIS DIRECTORY """
    try:
        print(f"{WARNING}{BOLD}COMPILING...{ENDC}")
        sb.call(f"g++ {FILE}", shell=True)
    except:
        print(f"{FAIL}{BOLD}COMPILATION ERROR...{ENDC}")
        finish()
        return

    print(f"{WARNING}{BOLD}CREATING SPECIFIED DIRECTORIES...{ENDC}")
    try:
        """ CREATE ALL DIRECTORIES NEEDED FOR TEST """
        os.mkdir(f"{TEST_ROOT}")
        os.mkdir(f"{RESULT_FILE_ROOT}")
        os.mkdir(f"{IN_FILE_ROOT}")
        os.mkdir(f"{OUT_FILE_ROOT}")
    except:
        shutil.rmtree(f"{TEST_ROOT}")
        os.mkdir(f"{TEST_ROOT}")
        os.mkdir(f"{RESULT_FILE_ROOT}")
        os.mkdir(f"{IN_FILE_ROOT}")
        os.mkdir(f"{OUT_FILE_ROOT}")

    """ GENERATE FILES FOR TESTS I/O """
    run()

    """ RUN THE .exe FILE, GET I/O FROM SPECIFIED FILES """
    for i in range(NUM_OF_TESTS):
        sb.call("cd target", shell=True)
        try:
            sb.call(
                f"a.exe < {IN_FILE_ROOT}/in-{i+1}.txt > {RESULT_FILE_ROOT}/result-{i+1}.txt", shell=True, timeout=3.0)
            sb.call("cd ..", shell=True)
        except:
            print(f"{FAIL}{BOLD}RUNTIME ERROR{ENDC}")
            finish()
            break
    try:
        os.remove("a.exe")
    except: 
        os.system("taskkill /f /im  a.exe")
        os.remove("a.exe")

    """ CHECK IF EXPECTED RESULT IS EQUAL WITH CLIENT'S ANSWER """
    for i in range(NUM_OF_TESTS):
        """ JUDGE CODE OUTPUT """
        try:
            expected_answer = [line.strip() for line in open(
                f"{OUT_FILE_ROOT}/out-{i+1}.txt", 'r').readlines()]
            """ CLIENT CODE OUTPUT """
            got_answer = [line.strip() for line in open(
                f"{RESULT_FILE_ROOT}/result-{i+1}.txt", 'r').readlines()]
        except:
            break

        test_result = True

        """ CHECK IF ALL THE OUTPUT LINES ARE EQUAL """
        for index, line in enumerate(expected_answer):
            try:
                if line.strip().strip("\n") != got_answer[index].strip().strip("\n"):
                    test_result = False
                    break
            except:
                test_result = False
                break

        if test_result:
            print(f"{OKGREEN}TEST {i+1} PASSED, SUCCESSFULLY{ENDC}")
        else:
            print(f"{FAIL}TEST {i+1} FAILED{ENDC}")
            print(f"{WARNING}\t- EXPECTED: {BOLD}{UNDERLINE}{expected_answer}{ENDC}")
            print(f"{FAIL}\t- GOT: {BOLD}{UNDERLINE}{got_answer}{ENDC}")
