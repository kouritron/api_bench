# run some wrk tests.

import os
import sys
import json
import time
import random
import subprocess as sp

from pathlib import Path
import shutil

# ======================================================================================================================
# ======================================================================================================================
ANSI_RED = "\u001b[31m"
ANSI_GREEN = "\u001b[32m"
ANSI_YELLOW = "\u001b[33m"
ANSI_BLUE = "\u001b[34m"
ANSI_MAGENTA = "\u001b[35m"
ANSI_CYAN = "\u001b[36m"
ANSI_RESET = "\u001b[0m"

_SEP_LINE = ANSI_YELLOW + ('-' * 80) + ANSI_RESET


# ======================================================================================================================
# ======================================================================================================================
def read_url():
    # TODO read url or just port from user.

    res = input(f'please supply the URL of the server to benchmarked.')

    return res


def run_benchmarks():

    url = read_url()

    cmnd_1 = f"""
# -c is connections
# -d is time in seconds
# -t is number of threads
# ./wrk -c 10 -t 8 -d 30 http://localhost:7081
./wrk -c 10 -t 8 -d 30 {url}

"""

    exit_code = sp.call(cmnd_1, shell=True)
    print(f'exit code: {exit_code}')


# ======================================================================================================================
# ======================================================================================================================
if '__main__' == __name__:

    start_time = time.time()

    print(f"**** Running {__file__}")

    repo_root = (Path(__file__) / '..' / '..').resolve()
    print(f'repo root appears to be: {repo_root}')
    print(_SEP_LINE)

    wrk_tmp_path = Path(repo_root / 'tmp_wrk').resolve()

    print(_SEP_LINE)
    print(f'Program finished. Time elapsed: {time.time() - start_time}')
