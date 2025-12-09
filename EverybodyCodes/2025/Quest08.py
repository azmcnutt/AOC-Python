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
    # # # # # # # # # # # # # # # # # # # # # #
    # --- Quest 8: The Art of Connection ---  #
    # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """1,5,2,6,8,4,1,7,3""",
        '2': """1,5,2,6,8,4,1,7,3,5,7,8,2""",
        '3': """1,5,2,6,8,4,1,7,3,6""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=8, event=2025)# ["1"].splitlines()
    nails = 32
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    ecd_data = [int(num) for num in ecd_input['1'].split(',')]
    cur_nail = 0
    rays = []
    for n in ecd_data:
        if cur_nail == 0:
            cur_nail = n
            continue
        if ((cur_nail < n and cur_nail + (nails / 2) == n) 
            or (n < cur_nail and n + (nails / 2) == cur_nail)):
            p1 += 1
        cur_nail = n

    # Part two
    nails = 256
    ecd_data = [int(num) for num in ecd_input['2'].split(',')]
    cur_nail = 0
    rays = []
    for n in ecd_data:
        if cur_nail == 0:
            cur_nail = n
            continue
        if n < cur_nail:
            t = (n, cur_nail)
        else:
            t = (cur_nail, n)
        count = 0
        for r in rays:
            if t[0] in r or t[1] in r:
                # Starts or ends at one of our ends
                pass
            elif (t[0] < r[0] < t[1]) and (t[0] < r[1] <t[1]):
                # ray is below t
                pass
            elif ((t[1] < r[0] <= nails) or (1 <= r[0] < t[0])
                  and (t[1] < r[1] <= nails) or (1 <= r[1] < t[0])):
                # ray is above t
                pass
            else:
                # We cross
                count += 1
        p2 += count
        if n < cur_nail:
            rays.append((n, cur_nail))
        else:
            rays.append((cur_nail, n))
        cur_nail = n

    # Part three
    nails = 256
    ecd_data = [int(num) for num in ecd_input['3'].split(',')]
    cur_nail = 0
    rays = []
    for n in ecd_data:
        if cur_nail == 0:
            cur_nail = n
            continue
        if n < cur_nail:
            rays.append((n, cur_nail))
        else:
            rays.append((cur_nail, n))
        cur_nail = n
    for t1 in range(1, nails + 1):
        for t2 in range(t1 + 1, nails + 1):
            t = (t1, t2)
            if t == (3, 7):
                pass
            count = 0
            for r in rays:
                if t[0] in r or t[1] in r:
                    # Starts or ends at one of our ends
                    pass
                elif (t[0] < r[0] < t[1]) and (t[0] < r[1] <t[1]):
                    # ray is below t
                    pass
                elif ((t[1] < r[0] <= nails) or (1 <= r[0] < t[0])
                    and (t[1] < r[1] <= nails) or (1 <= r[1] < t[0])):
                    # ray is above t
                    pass
                else:
                    # We cross
                    count += 1
            if t in rays:
                # add one if the cut matches a ray
                count += 1
            if count > p3:
                p3 = count
        
    
    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 