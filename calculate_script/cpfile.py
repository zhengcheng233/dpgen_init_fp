#!/usr/bin/env python

import os
from glob import glob 

dirs = glob('./iter.*/02.fp/data.*')

for dir0 in dirs:
    #dir0 = os.path.abspath(dir0)
    dir_n = (dir0[2:])
    dir_n1 = os.path.join('./databack',dir_n)
    #print(dir_n1)
    os.system('mkdir -p '+dir_n1)
    os.system('cp -r '+dir_n+'/* '+dir_n1)
