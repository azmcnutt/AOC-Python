# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from tqdm import tqdm
from ecd import get_inputs
import time


def main():
    # # # # # # # # # # # # # # # # # # # # # #
    # --- Quest 04: Whispers in the Shell --- #
    # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = """Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=1, event=2025)["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = ""
    p2 = 0
    names = ecd_input[0].split(',')
    instructions = ecd_input[2].split(',')
    position = 0
    for i in instructions:
        if i[0] == 'R':
            position += int(i[1:])
            if position >= len(names):
                position = len(names) - 1
        elif i[0] == 'L':
            position -= int(i[1:])
            if position < 0:
                position = 0
        print(names[position])
    p1 = names[position]

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')
    

if __name__ == '__main__':
    main()
 