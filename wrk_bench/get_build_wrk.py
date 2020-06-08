# get wrk, and do a small test or show the commands for it.

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

_WRK_SETUP_CMND = r"""
git clone https://github.com/wg/wrk .

make -j16

mv ./wrk ../wrk_executable
cd ..
rm -rf tmp_wrk

mkdir -p tmp_wrk
cd tmp_wrk
mv ../wrk_executable ./wrk

"""

# ======================================================================================================================
# ======================================================================================================================
if '__main__' == __name__:

    start_time = time.time()

    print(f"**** Running {__file__}")

    repo_root = (Path(__file__) / '..' / '..').resolve()
    print(f'repo root appears to be: {repo_root}')
    print(_SEP_LINE)

    wrk_tmp_path = Path(repo_root / 'tmp_wrk').resolve()

    # rm the tmp dirs if they exists and make new ones.
    shutil.rmtree(wrk_tmp_path, ignore_errors=True)

    # make new tmp dirs
    wrk_tmp_path.mkdir(parents=True, exist_ok=True)

    os.chdir(wrk_tmp_path)

    exit_code = sp.call(_WRK_SETUP_CMND, shell=True)

    print(_SEP_LINE)
    print(f'exit_code: {exit_code}, time elapsed: {time.time() - start_time}')
