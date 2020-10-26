#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 08:42:23 2018

@author: admin
"""

from CheckSudokuSolution import isValid

def main():
    # Read a Sudoku solution
    grid = readASolution()

    if isValid(grid):
        print("Valid solution")
    else:
        print("Invalid solution")

# Read a Sudoku solution from the console
def readASolution():
    grid = []
    with open('input1.txt') as f:
        for line in f:
            grid.append([eval(x) for x in line.strip().split()])

    return grid

def run():
    main()