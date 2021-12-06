#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    # print("Yes") if all([True if x in magazine and note.count(x) <= magazine.count(x) else False for x in note]) else print("No")
    g = Counter(note)
    f = Counter(magazine)
    print("Yes") if all([True if k in f.keys() and g[k] <= f[k] else False for k,v in g.items()]) else print("No")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
