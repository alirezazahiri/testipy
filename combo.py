import shutil
import os
from constants.COLORS import *
from constants.settings import INPUT_FILES_ROOT, SCORE_STATISTICS_FILE, TARGET_ROOT
from core.run_samples import execute
import threading
import subprocess as sb

lock = threading.Lock()

files = os.listdir(INPUT_FILES_ROOT)
with open(SCORE_STATISTICS_FILE, "w") as initialize:
    print(end='file name,coverage\n', file=initialize)
initialize.close()

files = [file for file in files if file.split('.')[1] in ['c', 'cpp']]
threads = []
results = []

def init():
    if not "main.cpp" in os.listdir("target"):
        sb.call("touch target/main.cpp")

init()

def pre_execute(target_root: str, filename: str):
    lock.acquire()
    results.append(execute(target_root, filename))
    lock.release()


for index, file in enumerate(files):
    print(f"{WARNING}{BOLD}RUNNING TESTS FOR {file}...{ENDC}")

    shutil.copyfile(rf"{INPUT_FILES_ROOT}/{file}",
                    rf"{TARGET_ROOT}/main.cpp")

    thread = threading.Thread(target=pre_execute(
        f"{TARGET_ROOT}/main.cpp", file))
    thread.start()
    threads.append(thread)

    print(f"{WARNING}{BOLD}FINISHED TESTING PROCESS ON {file}{ENDC}")

    with open(SCORE_STATISTICS_FILE, "a") as scores_file:
        print(results[index], file=scores_file)
    scores_file.close()

for thread in threads:
    thread.join()
