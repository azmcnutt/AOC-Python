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
    # # # # # # # # # # # # # # # # # #
    # --- Day 01: Secret Entrance --- #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=1, year=2025).splitlines()

    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    
    position = 50
    for line in tqdm(aoc_input):
        # p2 += move_dial_p2(position, line)
        position, roll_count = move_dial_p1(position, line)
        p2 += roll_count
        if position == 0:
            p1 += 1

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def move_dial_p1(dial, rotate):
    rollover_count = 0
    if rotate.startswith('L'):
        position = (dial - int(rotate[1:])) % 100
        if (dial - int(rotate[1:])) <= 0:
            if dial != 0:
                # Add one rollover if we are not at zero.
                dial -= 100
            rollover_count = abs(dial - int(rotate[1:])) // 100
    elif rotate.startswith('R'):
        position = (dial + int(rotate[1:])) % 100
        if (dial + int(rotate[1:])) >= 100:
            rollover_count = (dial + int(rotate[1:])) // 100
    else:
        raise ValueError(f'Invalid rotate command: {rotate}')
    return position, rollover_count

if __name__ == '__main__':
    main()
 