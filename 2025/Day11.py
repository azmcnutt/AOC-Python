# import os
# import sys
import copy
# from pprint import pprint
from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time
from pprint import pprint

def main():
    # # # # # # # # # # # # # #
    # --- Day 11: Reactor --- #
    # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=11, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    path = {}
    for l in aoc_input:
        k, p = l.split(': ')
        p = p.split()
        path[k] = p
    
    p1 = walk_path('you', path)
    
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def walk_path(loc, path):
    if path[loc][0] == 'out':
        return 1
    count = 0
    for l in path[loc]:
        count += walk_path(l, path)
    return count


if __name__ == '__main__':
    main()
 