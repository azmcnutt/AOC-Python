# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # # # #
    # --- Day 04: Printing Department --- #
    # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=4, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    dirs = [
        (0, 1), (1, 0), (0, -1), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1),
        ]

    p1 = 0
    p2 = 0
    first_run = True
    rolls_removed = []

    while first_run or rolls_removed:
        rolls_removed = []
        for y, line in enumerate(aoc_input):
            for x, char in enumerate(line):
                if char == '@':
                    # count number of adjacent rolls
                    count = 0
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(line) and 0 <= ny < len(aoc_input):
                            if aoc_input[ny][nx] == '@':
                                count += 1
                    if count <= 3:
                        if first_run:
                            p1 += 1
                        rolls_removed.append((x, y))
                        p2 += 1
        first_run = False
        # remove rolls that have been counted
        for x, y in rolls_removed:
            aoc_input[y] = aoc_input[y][:x] + '.' + aoc_input[y][x+1:]

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')
    

if __name__ == '__main__':
    main()
 