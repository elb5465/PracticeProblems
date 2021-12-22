#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countPalindromes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def countPalindromes(s):
    pCount, index, ws = 0,0,1        #palindrom count, WindowSize and starting place
    
    while not (ws > len(s)):
        substring = s[index:ws+index]
        if reversed(substring) == substring:     #palindrome
            pCount += 1
            
        if ws+index == len(s):
            index = 0
            ws += 1
        else: 
            index += 1
    
    return pCount
        
        
def reversed(s):
    return s[::-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = countPalindromes(s)

    fptr.write(str(result) + '\n')

    fptr.close()
