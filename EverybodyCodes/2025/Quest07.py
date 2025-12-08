# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from tqdm import tqdm
from ecd import get_inputs
import math
import time
from pprint import pprint
from copy import deepcopy
import re
import functools


GENERATED_NAMES = set()

def main():
    # # # # # # # # # # # # # # # #
    # --- Quest 7: Namegraph ---  #
    # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """Oronris,Urakris,Oroneth,Uraketh

r > a,i,o
i > p,w
n > e,r
o > n,m
k > f,r
a > k
U > r
e > t
O > r
t > h""",
        '2': """Xanverax,Khargyth,Nexzeth,Helther,Braerex,Tirgryph,Kharverax

r > v,e,a,g,y
a > e,v,x,r
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i""",
        '3': """Khara,Xaryt,Noxer,Kharax

r > v,e,a,g,y
a > e,v,x,r,g
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=7, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    ecd_data = ecd_input['1'].splitlines()
    names = ecd_data[0].split(',')
    rules = []
    test = []
    for r in ecd_data[2:]:
        r = r.split(' > ')
        r[1] = r[1].split(',')
        rules.append(r)

    for name in names:
        passed = True
        for rule in rules:
            target_pattern = r"[" + rule[0] + "]"
            occurrences = [match.start() for match in re.finditer(target_pattern, name)]
            for o in occurrences:
                if o + 1 >= len(name):
                    passed = False
                    break
                if name[o + 1] not in rule[1]:
                    passed = False
                    break
            if not passed:
                break
        if passed:
            test.append(name)
    
    if len(test) != 1:
        print('ERROR')
    else:
        p1 = test[0]
    
    # Part two
    ecd_data = ecd_input['2'].splitlines()
    names = ecd_data[0].split(',')
    rules = []
    test = []
    for r in ecd_data[2:]:
        r = r.split(' > ')
        r[1] = r[1].split(',')
        rules.append(r)

    for indx, name in enumerate(names):
        passed = True
        for rule in rules:
            target_pattern = r"[" + rule[0] + "]"
            occurrences = [match.start() for match in re.finditer(target_pattern, name)]
            for o in occurrences:
                if o + 1 >= len(name):
                    # passed = False
                    break
                if name[o + 1] not in rule[1]:
                    passed = False
                    break
            if not passed:
                break
        if passed:
            p2 += indx + 1
    
    # Part three
    ecd_data = ecd_input['3'].splitlines()
    names = ecd_data[0].split(',')
    rules = []
    test = []
    for r in ecd_data[2:]:
        r = r.split(' > ')
        r[1] = r[1].split(',')
        rules.append(r)
    
    for name in names:
        passed = True
        for rule in rules:
            target_pattern = r"[" + rule[0] + "]"
            occurrences = [match.start() for match in re.finditer(target_pattern, name)]
            for o in occurrences:
                if o + 1 >= len(name):
                    # passed = False
                    break
                if name[o + 1] not in rule[1]:
                    passed = False
                    break
            if not passed:
                break
        if passed:
            test.append(name)

    for name in test:
        generate_names(name, rules)
        p3 = len(GENERATED_NAMES)
    
    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

def generate_names(name, rules):
    count = 0
    if len(name) >= 7:
        GENERATED_NAMES.add(name)
    if len(name) < 11:
        for rule in rules:
            if name[-1] == rule[0]:
                for r in rule[1]:
                    generate_names(name + r, rules)

if __name__ == '__main__':
    main()
 