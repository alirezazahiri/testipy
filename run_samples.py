import subprocess as sb
import os 
import shutil
import sys 
sys.path.append(".")
from constants import IN_FILE_ROOT, NUM_OF_TESTS, OUT_FILE_ROOT, RESULT_FILE_ROOT, TEST_ROOT
from COLORS import *

""" RUN ANY .cpp FILE INSIDE THIS DIRECTORY """
print(f"{OKBLUE}COMPILING .cpp CODE...{ENDC}")
sb.call("g++ *.cpp", shell=True)

try:
    """ CREATE ALL DIRECTORIES NEEDED FOR TEST """
    os.mkdir(f"{TEST_ROOT}")
    os.mkdir(f"{RESULT_FILE_ROOT}")
    os.mkdir(f"{IN_FILE_ROOT}")
    os.mkdir(f"{OUT_FILE_ROOT}")
except:
    pass

""" GENERATE FILES FOR TESTS I/O """
sb.call("py file_gen.py", shell=True)

""" RUN THE .exe FILE, GET I/O FROM SPECIFIED FILES """
for i in range(NUM_OF_TESTS):
    sb.call(f"a.exe < {IN_FILE_ROOT}/in-{i+1}.txt > {RESULT_FILE_ROOT}/result-{i+1}.txt", shell=True)

""" CHECK IF EXPECTED RESULT IS EQUAL WITH CLIENT'S ANSWER """
for i in range(NUM_OF_TESTS):
    expected_answer = [line.strip().split() for line in open(f"{OUT_FILE_ROOT}/out-{i+1}.txt", 'r').readlines()][0]
    got_answer = [line.strip() for line in open(f"{RESULT_FILE_ROOT}/result-{i+1}.txt", 'r').readlines()]

    test_result = True

    """ CHECK IF ALL THE OUTPUT LINES ARE EQUAL """
    for index, line in enumerate(expected_answer):
        if line.strip().strip("\n") != got_answer[index].strip().strip("\n"):
            test_result = False
            break
    
    if test_result:
        print(f"{OKGREEN}TEST {i+1} PASSED, SUCCESSFULLY{ENDC}")
    else:
        print(f"{FAIL}TEST {i+1} FAILED{ENDC}")
        print(f"{WARNING}\t- EXPECTED: {BOLD}{UNDERLINE}{expected_answer}{ENDC}")
        print(f"{FAIL}\t- GOT: {BOLD}{UNDERLINE}{got_answer}{ENDC}")

""" REMOVE ALL TEST FILES CREATED """
try:
    shutil.rmtree(f"{TEST_ROOT}")
except:
    print("NOT FOUND :(")