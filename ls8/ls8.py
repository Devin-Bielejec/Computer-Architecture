#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
import os


if __name__ == '__main__':
    cpu = CPU()
    
    if sys.argv[1] == "all":
        programs_to_run = ["call", "interrupts", "keyboard", 'mult', 'print8', 'printstr', 'sctest', 'stack', 'stackoverflow']
    else:
        programs_to_run = sys.argv[1:]
    
    path = "examples/"
    extension = ".ls8"
    for program in programs_to_run:
        cpu.load(path + program + extension)
    
    for program in programs_to_run:
        cpu.run()
        cpu.halted = True