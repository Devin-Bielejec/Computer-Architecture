#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
import os


if __name__ == '__main__':    
    if sys.argv[1] == "all":
        programs_to_run = ["call", 'mult', 'print8', 'sctest', 'stack']
    else:
        programs_to_run = sys.argv[1:]
    
    path = "examples/"
    extension = ".ls8"
    for program in programs_to_run:
        cpu = CPU()
        cpu.load(path + program + extension)
        print(f'PROGRAM: {program}')
        cpu.run()
    