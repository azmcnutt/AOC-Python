# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from tqdm import tqdm
from ecd import get_inputs
import time


def main():
    # # # # # # # # # # # # # # # # # # #
    # --- Quest 3: The Deepest Fit ---  #
    # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """10,5,1,10,3,8,5,2,2""",
        '2': """4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77""",
        '3': """4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=3, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    ecd_data = ecd_input['1'].splitlines()
    ecd_data = [int(num) for num in ecd_data[0].split(',')]
    ecd_data = set(ecd_data)
    p1 = sum(ecd_data)

    # Part two
    ecd_data = ecd_input['2'].splitlines()
    ecd_data = [int(num) for num in ecd_data[0].split(',')]
    ecd_data = list(set(ecd_data))
    ecd_data.sort()
    p2 = sum(ecd_data[:20])

    # Part three
    ecd_data = ecd_input['3'].splitlines()
    ecd_data = [int(num) for num in ecd_data[0].split(',')]
    crate_inventory = {}
    for crate in ecd_data:
        if crate in crate_inventory.keys():
            crate_inventory[crate] += 1
        else:
            crate_inventory[crate] = 1
    
    p3 = max(crate_inventory.values())

    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 