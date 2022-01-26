import shutil
import os
import subprocess as sb 
from constants.COLORS import *
from constants.settings import INPUT_FILES_ROOT, TARGET_ROOT
from settings.run_samples import execute


files = os.listdir(INPUT_FILES_ROOT)

for file in files: 
    if file.endswith(".cpp"):
        print(f"{WARNING}{BOLD}RUNNING TESTS FOR {file}...{ENDC}")
        # sb.call(f"cp {INPUT_FILES_ROOT}/{file} {TARGET_ROOT}/main.cpp", shell=True)
        shutil.copyfile(rf"{INPUT_FILES_ROOT}/{file}", rf"{TARGET_ROOT}/main.cpp")
        execute(f"{TARGET_ROOT}/main.cpp")
        print(f"{WARNING}{BOLD}FINISHED TESTING PROCESS ON {file}{ENDC}")
