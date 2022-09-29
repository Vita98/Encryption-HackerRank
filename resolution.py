#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    noSpaces = s.strip()
    L = len(noSpaces)
    
    row = math.floor(math.sqrt(L))
    column = math.ceil(math.sqrt(L))
    
    if row * column < L:
        if row < column:
            row += 1
        elif row > column or row == column:
            column += 1            
    
    currentCol = 0
    grid = []
    for i in range(row):
        
        if currentCol+column >= L:
            grid.append( noSpaces[currentCol::])
            break
        else:
            grid.append(noSpaces[currentCol:currentCol+column])
            currentCol += column
            
    encStr = ""
    for j in range(column):
        for i in range(row):
            if j < len(grid[i]):
                encStr += grid[i][j]
            
        encStr += " "
        
    return encStr
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
