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

    test_cases = """
 12 458: {'quality': 9199911763584, 'levels': [19, 16, 89, 19, 79, 12, 17, 479, 567, 136, 257, 38, 46]}
 13  56: {'quality': 9199911763584, 'levels': [19, 16, 89, 19, 79, 12, 17, 479, 567, 136, 257, 38, 34]}
 14 279: {'quality': 9199911763584, 'levels': [19, 16, 89, 19, 79, 12, 17, 479, 567, 136, 257, 38, 34]}
 
 19 206: {'quality': 8447433334444, 'levels': [189, 148, 247, 578, 145, 35, 36, 39, 34, 349, 47, 4, 4]}
 20 101: {'quality': 8447433334444, 'levels': [189, 148, 247, 578, 145, 35, 36, 39, 34, 49, 47, 47, 4]}
 25 323: {'quality': 7141611995448, 'levels': [579, 15, 247, 18, 167, 15, 13, 49, 69, 358, 149, 46, 8]}
 26 329: {'quality': 7141611995448, 'levels': [579, 15, 247, 18, 167, 15, 13, 49, 69, 358, 49, 46, 89]}
 
 29 212: {'quality': 6555555555555, 'levels': [267, 258, 157, 158, 259, 259, 357, 59, 58, 58, 5, 5, 5]}
 30 369: {'quality': 6555555555555, 'levels': [267, 258, 157, 158, 259, 259, 257, 59, 58, 58, 5, 5, 5]}
 31 182: {'quality': 6555555555555, 'levels': [267, 158, 157, 258, 258, 259, 59, 57, 59, 58, 58, 5, 5]}

 42 248: {'quality': 5285913723855, 'levels': [258, 126, 389, 259, 89, 15, 138, 478, 26, 34, 38, 5, 5]}
 43 327: {'quality': 5285913723855, 'levels': [258, 126, 389, 259, 89, 15, 138, 478, 26, 34, 38, 5, 5]}
 
 48  35: {'quality': 5119999739386, 'levels': [356, 17, 19, 69, 59, 59, 89, 178, 135, 49, 35, 789, 68]}
 49 500: {'quality': 5119999739386, 'levels': [356, 17, 19, 69, 49, 59, 89, 178, 135, 49, 35, 789, 68]}
 50 214: {'quality': 5119999739386, 'levels': [356, 17, 19, 69, 59, 59, 89, 178, 135, 49, 35, 789, 68]}
 
 52 177: {'quality': 4654112937422, 'levels': [349, 369, 456, 145, 15, 12, 26, 79, 236, 37, 247, 2, 2]}
 53 307: {'quality': 4654112937422, 'levels': [348, 369, 456, 145, 15, 12, 26, 79, 236, 37, 247, 2, 2]}
 60 486: {'quality': 2999475311113, 'levels': [128, 29, 69, 79, 146, 679, 157, 235, 16, 17, 16, 19, 3]}
 61 143: {'quality': 2999475311113, 'levels': [128, 29, 69, 39, 146, 679, 157, 235, 16, 17, 16, 19, 3]}
 63 403: {'quality': 2637777555553, 'levels': [128, 469, 235, 27, 17, 47, 17, 357, 156, 25, 45, 15, 3]}
 64 159: {'quality': 2637777555553, 'levels': [128, 469, 235, 27, 17, 47, 17, 357, 15, 25, 45, 15, 35]}"""
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
 