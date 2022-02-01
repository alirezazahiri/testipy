import subprocess as sb
import os
import shutil
from core.file_gen import run_file_gen
from constants.COLORS import *
from constants.settings import IN_FILE_ROOT, NUM_OF_TESTS, OUT_FILE_ROOT, RESULT_FILE_ROOT, TEST_ROOT, TARGET_ROOT


def finish():
    """ REMOVE ALL TEST FILES CREATED """
    try:
        shutil.rmtree(f"{TEST_ROOT}")
    except:
        return


def make_dirs():
    os.mkdir(f"{TEST_ROOT}")
    os.mkdir(f"{RESULT_FILE_ROOT}")
    os.mkdir(f"{IN_FILE_ROOT}")
    os.mkdir(f"{OUT_FILE_ROOT}")


def execute(FILE: str, input_code_filename: str):
    """ RUN ANY .cpp FILE INSIDE THIS DIRECTORY """
    try:
        print(f"{WARNING}{BOLD}COMPILING...{ENDC}")
        compilation_response = sb.call(f"g++ {FILE}", shell=True)
        exe_exists = "a.exe" in os.listdir(".")

        if not exe_exists:
            print(
                f"{FAIL}{BOLD}COMPILATION ERROR...(CODE: {FAIL}{UNDERLINE}{BOLD}{compilation_response}{ENDC}){ENDC}")
            finish()
            return "COMPILE FAILED!"
    except:
        print(f"{FAIL}{BOLD}COMPILATION ERROR...{ENDC}")
        finish()
        return "COMPILE FAILED!"

    print(f"{WARNING}{BOLD}CREATING SPECIFIED DIRECTORIES...{ENDC}")
    try:
        """ CREATE ALL DIRECTORIES NEEDED FOR TEST """
        make_dirs()
    except:
        shutil.rmtree(f"{TEST_ROOT}")
        make_dirs()

    """ GENERATE FILES FOR TESTS I/O """
    run_file_gen()

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

    passed_tests_count = 0

    for i in range(NUM_OF_TESTS):
        try:
            """ JUDGE CODE OUTPUT """
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
            passed_tests_count += 1
        else:
            print(f"{FAIL}TEST {i+1} FAILED{ENDC}")
            print(f"{WARNING}\t- EXPECTED: {BOLD}{UNDERLINE}{expected_answer}{ENDC}")
            print(f"{FAIL}\t- GOT: {BOLD}{UNDERLINE}{got_answer}{ENDC}")

    print(f"{OKCYAN}{BOLD}PASSED {OKGREEN}{passed_tests_count}{ENDC} {OKCYAN}{BOLD}TESTS OUT OF {WARNING}{NUM_OF_TESTS}{ENDC}")
    print(f"\t{OKCYAN} SCORE OF {input_code_filename} {WARNING}->{OKBLUE} {round(passed_tests_count*100/NUM_OF_TESTS, 2)}%")
    return f"{input_code_filename},{round(passed_tests_count*100/NUM_OF_TESTS, 2)}%"
