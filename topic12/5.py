#!/bin/python3

import math
import os
import random
import re
import sys

all_combination = dict()

def create_combination(contact):
    return [contact[0:i] for i in range(1, len(contact)+1)]

def add(contact):
    global all_combination
    for comb in create_combination(contact):
        all_combination[comb] = all_combination.get(comb, 0) + 1

def find(name):
    global all_combination
    return all_combination.get(name, 0)
        
if __name__ == '__main__':
    n = int(input().strip())

    for n_itr in range(n):
        op, contact = input().strip().split(' ')
        add(contact) if op == "add" else print(find(contact))
            
