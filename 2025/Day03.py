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
    # # # # # # # # # # # # #
    # --- Day 03: Lobby --- #
    # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=3, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    for line in tqdm(aoc_input):
        p1 += get_next_largest(line, 2)
        p2 += get_next_largest(line, 12)
    
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')
    
    
def get_next_largest(line, numbers_left):
    numbers_left -= 1
    digit = 0
    line_idx = 0
    for idx in range(0, len(line) - numbers_left):
        char = line[idx]
        if int(char) > digit:
            digit = int(char)
            line_idx = idx
    if numbers_left > 0:
        ret = get_next_largest(line[line_idx + 1:], numbers_left)
        return (digit * (10 ** numbers_left)) + ret
    else:
        return digit

if __name__ == '__main__':
    main()
 