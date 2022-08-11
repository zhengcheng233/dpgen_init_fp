#!/usr/bin/env python
import os
from glob import glob
import time
dirs = glob('./*/*/*/*.com')

cwd = os.getcwd()
for dir0 in dirs:
    f_name = os.path.basename(dir0)
    os.system('cp case1.slurm '+dir0[:-len(f_name)])
    os.system('cp gen_input_com.py '+dir0[:-len(f_name)])
    os.chdir(dir0[:-len(f_name)])
    os.system('python gen_input_com.py')
    time.sleep(0.1)
    os.system('sbatch case1.slurm')
    os.chdir(cwd)
