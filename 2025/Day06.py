# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time


def main():
    # # # # # # # # # # # # # # # # # #
    # --- Day 6: Trash Compactor ---  #
    # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=6, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    numbers = []
    operators = []

    for line in aoc_input:
        line = line.split()
        if is_integer_string(line[0]):
            numbers.append([int(x) for x in line])
        else:
            operators = line
    
    # Part 1
    for indx, op in enumerate(operators):
        sub_total = 0
        if op == '*':
            sub_total = 1
            for row in numbers:
                sub_total *= row[indx]
        elif op == '+':
            for row in numbers:
                sub_total += row[indx]
        p1 += sub_total

    # Part 2 
        problem = {
            'numbers_txt': {},
            'numbers_int': [],
            'operator': '',
        }
    for x in range(len(aoc_input[0]) + 1):
        end_of_problem = False
        if x + 1 > len(aoc_input[0]):
            end_of_problem = True
        elif x + 1 != len(aoc_input[0]):
            if aoc_input[-1][x + 1] in ['*', '+']:
                end_of_problem = True
        if end_of_problem:
            # blank row, solve this problem and go to the next
            problem['numbers_int'] = [int(x) for x in problem['numbers_txt'].values()]
            sub_total = 0
            if problem['operator'] == '*':
                sub_total = 1
                for num in problem['numbers_int']:
                    sub_total *= num
            elif problem['operator'] == '+':
                for num in problem['numbers_int']:
                    sub_total += num
            print(sub_total)
            p2 += sub_total
            problem = {
                'numbers_txt': {},
                'numbers_int': [],
                'operator': '',
            }
        else:
            for y in range(len(aoc_input)):
                if is_integer_string(aoc_input[y][x]):
                    if x not in problem['numbers_txt']:
                        problem['numbers_txt'][x] = aoc_input[y][x]
                    else:
                        problem['numbers_txt'][x] += aoc_input[y][x]
                elif aoc_input[y][x] in ['*', '+']:
                    problem['operator'] = aoc_input[y][x]
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def is_integer_string(s):
    """
    Checks if a given string can be successfully converted to an integer.

    Args:
        s: The string to check.

    Returns:
        True if the string can be converted to an integer, False otherwise.
    """
    try:
        int(s)  # Attempt to convert the string to an integer
        return True
    except ValueError:
        # If a ValueError occurs, the string cannot be converted to an integer
        return False

if __name__ == '__main__':
    main()
 