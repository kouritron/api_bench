import os
import sys
import json
import time
import random
import subprocess as sp

from pathlib import Path
import shutil

# ======================================================================================================================
# =============================================================================================================== PARAMS

_URL = 'http://localhost:7081'
_TIME = 10
_NUM_CONNS = 100
_NUM_CONNS = 400
_NUM_THREADS = 12
_NUM_THREADS = 16

# Example: 12 threads, 400 connections (fds, careful not to exceed max fds, or raise the limit)
# kept open at one time, run for 30 seconds.
# wrk -t12 -c400 -d30s _URL_

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


def run_benchmarks():

    print(f'\nGoing to hit: {_URL}')
    print(f'For {_TIME} seconds, using {_NUM_THREADS} threads, w/ {_NUM_CONNS} simultaneous connections.')

    cmnd = f"""
# -c is connections
# -d is time in seconds
# -t is number of threads
# ./wrk -c 10 -t 8 -d 30 http://localhost:7081

./wrk -t {_NUM_THREADS} -c {_NUM_CONNS} -d {_TIME} {_URL}

"""
    print(_SEP_LINE)
    exit_code = sp.call(cmnd, shell=True)
    print(_SEP_LINE)

    print(f'exit code: {exit_code}')


# ======================================================================================================================
# ======================================================================================================================
if '__main__' == __name__:

    start_time = time.time()

    print(f"**** Running {__file__}")

    repo_root = (Path(__file__) / '..' / '..').resolve()
    print(f'repo root appears to be: {repo_root}')

    wrk_tmp_path = Path(repo_root / 'tmp_wrk').resolve()
    os.chdir(wrk_tmp_path)

    # this assumes a working wrk executable is available at cwd
    run_benchmarks()

    print(f'Program finished. Time elapsed: {time.time() - start_time}')
