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
        '3': """1:7,1,9,1,6,9,8,3,7,2
2:6,1,9,2,9,8,8,4,3,1
3:7,1,9,1,6,9,8,3,8,3
4:6,1,9,2,8,8,8,4,3,1
5:7,1,9,1,6,9,8,3,7,3
6:6,1,9,2,8,8,8,4,3,5
7:3,7,2,2,7,4,4,6,3,1
8:3,7,2,2,7,4,4,6,3,7
9:3,7,2,2,7,4,1,6,3,7""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=5, event=2025)# ["1"].splitlines()
    # 31575811 First digit correct, length is correct.
    
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

    # Part three
    my_sort = []
    ecd_data = ecd_input['3'].splitlines()
    swords = {}
    for x in ecd_data:
        id, x = x.split(':')
        x= x.split(',')
        x = [int(num) for num in x]
        swords[int(id)] = _cal_strength(x)
    sorted_items = sorted(swords.items(), key=lambda item: item[1]['quality'])
    for s in sorted_items:
        if not my_sort:
            my_sort.append(s[0])
            continue
        for i, t in enumerate(my_sort):
            if s[0] in my_sort:
                break
            if swords[s[0]]['quality'] == swords[t]['quality']:
                # same quality, check levels
                for l in range(len(swords[s[0]]['levels'])):
                    if swords[s[0]]['levels'][l] > swords[t]['levels'][l]:
                        my_sort.insert(i, s[0])
                        break
                    elif swords[s[0]]['levels'][l] < swords[t]['levels'][l]:
                        my_sort.insert(i+1, s[0])
                        break
                my_sort.insert(i, s[0])
                break
            elif swords[s[0]]['quality'] > swords[t]['quality']:
                my_sort.insert(i, s[0])
                break
            elif swords[s[0]]['quality'] < swords[t]['quality']:
                my_sort.insert(i+1, s[0])
                break
    for index, val in enumerate(my_sort):
        p3 += val * (index + 1)
        print_it=False
        if index != 0:
            if swords[val]['quality'] == swords[my_sort[index - 1]]['quality']:
                print_it=True
        if index + 1 < len(my_sort):
            if swords[val]['quality'] == swords[my_sort[index + 1]]['quality']:
                print_it=True
        if print_it:
            print(f'{index:>3} {val:>3}: {swords[val]}')
    # p3 = max(swords) - min(swords)
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

def _cal_strength(data):
    count = 0
    hilt = {}
    ret = ''
    levels = []
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
        temp_level = ''
        ret += str(hilt[h]['c'])
        if 'l' in hilt[h].keys():
            temp_level += str(hilt[h]['l'])
        if 'c' in hilt[h].keys():
            temp_level += str(hilt[h]['c'])
        if 'r' in hilt[h].keys():
            temp_level += str(hilt[h]['r'])
        levels.append(int(temp_level))

    return {'quality': int(ret), 'levels': levels}

if __name__ == '__main__':
    main()
 