# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from tqdm import tqdm
from ecd import get_inputs
import math
import time


def main():
    # # # # # # # # # # # # # # # # # # # #
    # --- Quest 4: Teeth of the Wind ---  #
    # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """102
75
50
35
13""",
        '2': """102
75
50
35
13""",
        '3': """5
7|21
18|36
27|27
10|50
10|50
11""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=4, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    ecd_data = ecd_input['1'].splitlines()
    ecd_data = [int(num) for num in ecd_data]

    gr = _calc_total_gear_ratio(ecd_data)
    p1 = int(_calc_number_of_turns_out(2025, gr))

    # Part two
    ecd_data = ecd_input['2'].splitlines()
    ecd_data = [int(num) for num in ecd_data]

    gr = _calc_total_gear_ratio(ecd_data)
    p2 = math.ceil(_calc_number_of_turns_in(10000000000000, gr))

    # Part three
    pairs = []
    ecd_data = ecd_input['3']
    ecd_data = ecd_data.split('|')
    for pair in ecd_data:
        x, y = map(int, pair.split('\n'))
        pairs.append((x, y))
    gr = _calc_compound_gear_ratio(pairs)
    p3 = int(_calc_number_of_turns_out(100, gr))

    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

def _calc_total_gear_ratio(gear_list):
    total_ratio = 1.0
    for idx, gear in enumerate(gear_list[1:], start=1):
        total_ratio *= gear / gear_list[idx - 1]
    return total_ratio

def _calc_compound_gear_ratio(gear_pairs):
    total_ratio = 1.0
    for g in gear_pairs:
       total_ratio *= g[1] / g[0]
    return total_ratio

def _calc_number_of_turns_out(turns, ratio):
    return turns / ratio

def _calc_number_of_turns_in(turns, ratio):
    return turns * ratio

if __name__ == '__main__':
    main()
 