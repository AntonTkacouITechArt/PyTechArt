#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING expression as parameter.
#

def isBalanced(expression):
    stack = []
    if expression[0] in [')','}',']']:
        return "NO"
    for x in range(len(expression)):
        if expression[x] in ['(', '{', '[']:
            stack.append(expression[x])
        else:
            if len(stack) == 0:
                return "NO"
            y = stack.pop()
            if (y,expression[x]) not in [('(',')'), ('{','}'), ('[',']')]:
                return "NO"
    return "YES" if len(stack) == 0 else "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        expression = input()

        res = isBalanced(expression)

        fptr.write(res + '\n')

    fptr.close()
