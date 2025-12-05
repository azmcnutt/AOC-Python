# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from tqdm import tqdm
from ecd import get_inputs
import time


def main():
    # # # # # # # # # # # # # # # # # # # # # # #
    # --- Quest 2: From Complex to Clarity ---  #
    # # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """A=[25,9]""",
        '2': """A=[35300,-64910]""",
        '3': """A=[35300,-64910]""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=2, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    ecd_data = ecd_input['1'].splitlines()
    ax, ay = map(int, ecd_data[0].split('=')[1].strip('[]').split(','))
    rx = 0
    ry = 0
    rx, ry = calc(ax, ay, rx, ry)
    p1 = f'[{rx},{ry}]'

    # Part two
    ecd_data = ecd_input['2'].splitlines()
    ax, ay = map(int, ecd_data[0].split('=')[1].strip('[]').split(','))
    top_left = (ax, ay)
    bottom_right = _add(top_left, (1000, 1000))
    points_to_check = []
    for y in range(top_left[1], bottom_right[1] + 1, 10):
        for x in range(top_left[0], bottom_right[0] + 1, 10):        
            points_to_check.append((x, y))

    for p in tqdm(points_to_check, desc='Part 2 Progress', unit='points'):
        if _verify(p):
            p2 += 1
    
    # Part three
    for y in tqdm(range(top_left[1], bottom_right[1] + 1), desc='Part 3 Progress', unit='rows'):
        for x in range(top_left[0], bottom_right[0] + 1):
            if _verify((x, y)):
                p3 += 1



    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

def calc(ax, ay, rx, ry):
    for _ in range(3):
        # first multiply
        rx, ry = _mul((rx, ry), (rx, ry))
        # then divide
        rx, ry = _div((rx, ry), (10, 10))
        # then add
        rx, ry = _add((rx, ry), (ax, ay))
    return rx, ry

def _verify(point):
    test = (0,0)
    for _ in range(100):
        test = _mul(test, test)
        test = _div(test, (100000,100000))
        test = _add(test, point)
        if (not (-1000000 < test[0] < 1000000)) or (not (-1000000 < test[1] < 1000000)):
            return False
    return True

def _add(a, b):
    # [X1,Y1] + [X2,Y2] = [X1 + X2, Y1 + Y2]
    return (a[0] + b[0], a[1] + b[1])

def _mul(a, b):
    # [X1,Y1] * [X2,Y2] = [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def _div(a, b):
    # [X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2]
    return (int(a[0] / b[0]), int(a[1] / b[1]))




if __name__ == '__main__':
    main()
 