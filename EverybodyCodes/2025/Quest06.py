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


def main():
    # # # # # # # # # # # # # # # # # # # #
    # --- Quest 6: Mentorship Matrix ---  #
    # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """ABabACacBCbca""",
        '2': """AaAaa 
 BbBb
 CcCc""",
        '3': """AABCBABCABCabcabcABCCBAACBCa""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=6, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    a_mentors = 0
    b_mentors = 0
    c_mentors = 0
    ecd_data = ecd_input['1']
    for x in ecd_data:
        if x == 'A':
            a_mentors += 1
        elif x == 'a':
            p1 += a_mentors
    
    # Part two
    a_mentors = 0
    b_mentors = 0
    c_mentors = 0
    ecd_data = ecd_input['2']
    for x in ecd_data:
        if x == 'A':
            a_mentors += 1
        elif x == 'a':
            p2 += a_mentors
        elif x == 'B':
            b_mentors += 1
        elif x == 'b':
            p2 += b_mentors
        elif x == 'C':
            c_mentors += 1
        elif x == 'c':
            p2 += c_mentors
    
    # Part three
    repeats = 1000
    lookup_range = 1000
    ecd_data = ecd_input['3']
    full_map = ''
    for _ in range(repeats):
        full_map += ecd_data
    for indx, x in enumerate(full_map):
        if x == 'a':
            if indx - lookup_range < 0:
                start = 0
            else:
                start = indx - lookup_range
            if indx + lookup_range >= len(full_map):
                end = -1
            else:
                end = indx + lookup_range + 1
            # print(f'{indx}:{x} [{start}:{end}] = {full_map[start:end].count("A")}')
            p3 += full_map[start:end].count('A')
        if x == 'b':
            if indx - lookup_range < 0:
                start = 0
            else:
                start = indx - lookup_range
            if indx + lookup_range >= len(full_map):
                end = -1
            else:
                end = indx + lookup_range + 1
            # print(f'{indx}:{x} [{start}:{end}] = {full_map[start:end].count("B")}')
            p3 += full_map[start:end].count('B')
        if x == 'c':
            if indx - lookup_range < 0:
                start = 0
            else:
                start = indx - lookup_range
            if indx + lookup_range >= len(full_map):
                end = -1
            else:
                end = indx + lookup_range + 1
            # print(f'{indx}:{x} [{start}:{end}] = {full_map[start:end].count("B")}')
            p3 += full_map[start:end].count('C')
    
    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 