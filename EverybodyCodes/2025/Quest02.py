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
        '2': """A=[25,9]""",
        '3': """A=[25,9]""",
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
    # pass one
    rx, ry = calc(ax, ay, rx, ry)
    # pass two
    rx, ry = calc(ax, ay, rx, ry)
    # pass three
    rx, ry = calc(ax, ay, rx, ry)
    p1 = f'[{rx},{ry}]'


    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

def calc(ax, ay, rx, ry):
    # R = R * R = [0,0]
    # R = R / [10,10] = [0,0]
    # R = R + A = [25,9]
    # [X1,Y1] * [X2,Y2] = [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]
    # first multiply
    bx = rx
    by = ry
    rx = (bx * bx) - (by * by)
    ry = (bx * by) + (by * bx)
    #[X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2]
    # then divide
    rx = int(rx / 10)
    ry = int(ry / 10)
    # then add
    # [X1,Y1] + [X2,Y2] = [X1 + X2, Y1 + Y2]
    rx = rx + ax
    ry = ry + ay
    return rx, ry




if __name__ == '__main__':
    main()
 