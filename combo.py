import shutil
import os
from constants.COLORS import *
from constants.settings import INPUT_FILES_ROOT, SCORE_STATISTICS_FILE, TARGET_ROOT
from settings.run_samples import execute


files = os.listdir(INPUT_FILES_ROOT)
with open(SCORE_STATISTICS_FILE, "w") as initialize:
    print(end='', file=initialize)
initialize.close()

for file in files:
    if file.endswith(".cpp"):
        print(f"{WARNING}{BOLD}RUNNING TESTS FOR {file}...{ENDC}")
        shutil.copyfile(rf"{INPUT_FILES_ROOT}/{file}",
                        rf"{TARGET_ROOT}/main.cpp")
        response = execute(f"{TARGET_ROOT}/main.cpp", file)
        print(f"{WARNING}{BOLD}FINISHED TESTING PROCESS ON {file}{ENDC}")
        with open(SCORE_STATISTICS_FILE, "a") as scores_file:
            print(response, file=scores_file)
        scores_file.close()
