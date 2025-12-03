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
    # --- Day 02: Gift Shop ---       #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=2, year=2025)
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    for range_pair in tqdm(aoc_input.split(',')):
        part1, part2 = range_pair.split('-')
        part1 = int(part1)
        part2 = int(part2)
        if part1 <= part2:
            low = part1
            high = part2
        else:
            low = part2
            high = part1
        for test in range(low, high + 1):
            product_id = str(test)
            midpoint = len(product_id) // 2
            if len(product_id) % 2 == 0 and product_id[:midpoint] == product_id[midpoint:]:
                p2 += test
                p1 += test
            elif product_id in (product_id + product_id)[1:-1]:
                p2 += test

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 