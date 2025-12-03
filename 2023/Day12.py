import math
import os
import sys
import copy
from pprint import pprint
from aocd import get_data, submit
import time
from math import trunc
import re
from functools import lru_cache

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# --- Day 12: Hot Springs ---                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/
# load sample data, copied and pasted from the site into list.  Each list item is one line of input

myset = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()

# once the test data provides the right answer: replace test data with data from the puzzle input

# myset = get_data(day=12, year=2023).splitlines()

# get the time we start running our solution: even though I'm running in debug mode
start_time = time.time()
p1ans = 0
p2ans = 0

for row in myset:
    springs, groups = row.split(' ')
    groups = groups.split(',')
    groups_list = []
    for i in groups:
        groups_list.append(int(i))
    groups = tuple(groups_list)

    print(f'{springs}, {groups} ({type(groups)})')

print(f'P1: {p1ans} and P2: {p2ans} in {time.time() - start_time} seconds.')
