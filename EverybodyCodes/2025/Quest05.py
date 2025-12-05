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
    # # # # # # # # # # # # # # # # # #
    # --- Quest 5: Fishbone Order --- #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """58:5,3,7,8,9,10,4,5,7,8,8""",
        '2': """1:2,4,1,1,8,2,7,9,8,6
2:7,9,9,3,8,3,8,8,6,8
3:4,7,6,9,1,8,3,7,2,2
4:6,4,2,1,7,4,5,5,5,8
5:2,9,3,8,3,9,5,2,1,4
6:2,4,9,6,7,4,1,7,6,8
7:2,3,7,6,2,2,4,1,4,2
8:5,1,5,6,8,3,1,8,3,9
9:5,7,7,3,7,2,3,8,6,7
10:4,1,9,3,8,5,4,3,5,5""",
        '3': """58:5,3,7,8,9,10,4,5,7,8,8""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    # ecd_input = get_inputs(quest=5, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    ecd_data = ecd_input['1'].splitlines()
    ecd_data = ecd_data[0].split(':')[1].split(',')
    ecd_data = [int(num) for num in ecd_data]
    p1 = _cal_fishbone(ecd_data)

    # Part two
    ecd_data = ecd_input['2'].splitlines()
    swords = []
    for x in ecd_data:
        x = x.split(':')[1].split(',')
        x = [int(num) for num in x]
        swords.append(_cal_fishbone(x))
    p2 = max(swords) - min(swords)

    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')
    
def _cal_fishbone(data):
    count = 0
    hilt = {}
    ret = ''
    for x in data:
        placed = False
        if len(hilt.keys()) == 0:
            hilt[count] = {'c': x}
        else:
            for h in range(len(hilt.keys())):
                if x < hilt[h]['c'] and 'l' not in hilt[h].keys():
                    hilt[h]['l'] = x
                    placed = True
                    break
                elif x > hilt[h]['c'] and 'r' not in hilt[h].keys():
                    hilt[h]['r'] = x
                    placed = True
                    break
            if not placed:
                count += 1
                hilt[count] = {'c': x}
    for h in hilt:
        ret += str(hilt[h]['c'])
    return int(ret)

if __name__ == '__main__':
    main()
 