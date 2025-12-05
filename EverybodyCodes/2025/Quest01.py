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
    # --- Quest 1: Whispers in the Shell ---  #
    # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1""",
        '2': """Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1""",
        '3': """Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L3
""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=1, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = ''
    p2 = ''
    p3 = ''

    # Part one - Pointer stops at the edge
    ecd_one = ecd_input['1'].splitlines()
    names = ecd_one[0].split(',')
    instructions = ecd_one[2].split(',')
    number_of_names = len(names)
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
    p1 = names[position]

    # Part Two - Pointer wraps around
    ecd_one = ecd_input['2'].splitlines()
    names = ecd_one[0].split(',')
    instructions = ecd_one[2].split(',')
    number_of_names = len(names)
    position = 0
    for i in instructions:
        if i.startswith('R'):
            position = (position + int(i[1:])) % number_of_names
        elif i.startswith('L'):
            position = (position - int(i[1:])) % number_of_names
    p2 = names[position]

    # Part Two - Pointer swaps
    ecd_one = ecd_input['3'].splitlines()
    names = {}
    count = 0
    for n in ecd_one[0].split(','):
        names[count] = n
        count += 1
    instructions = ecd_one[2].split(',')
    number_of_names = len(names)
    for i in instructions:
        position = 0
        if i.startswith('R'):
            position = (position + int(i[1:])) % number_of_names
        elif i.startswith('L'):
            position = (position - int(i[1:])) % number_of_names
        names[0], names[position] = names[position], names[0]
    p3 = names[0]

    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')
    

if __name__ == '__main__':
    main()
 