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
    # # # # # # # # # # # # # # #
    # --- Day 5: Cafeteria ---  #
    # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=5, year=2025).splitlines()
    # Too high 434607844413936
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    ranges = []
    ingredients = []

    for line in aoc_input:
        if '-' in line:
            a, b = line.split('-')
            ranges.append((int(a), int(b)))
        elif line:
            ingredients.append(int(line))
    
    for ingredient in tqdm(ingredients):
        if check_ranges(ingredient, ranges):
            p1 += 1
    
    ranges = merge_intervals(ranges)

    for range in tqdm(ranges):
        a, b = range
        p2 += (b - a + 1)

    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def check_ranges(ingredient, ranges):
    for a, b in ranges:
        if a <= ingredient <= b:
            return True
    return False

def merge_intervals(intervals):
    """
    Merge overlapping and adjacent intervals into a list of non-overlapping intervals.

    Args:
        intervals (list of tuples): List of intervals represented as tuples (start, end).

    Returns:
        merged (list of tuples): List of non-overlapping intervals after merging.
    """
    # 1. Sort the intervals based on their start times.
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # 2. Initialize the merged list with the first interval.
    merged = [sorted_intervals[0]]

    # 3. Iterate through the rest of the sorted intervals.
    for current_start, current_end in tqdm(sorted_intervals[1:]):
        # Get the end time of the last interval added to the merged list.
        last_end = merged[-1][1]

        # Check for overlap or adjacency.
        # If the current interval starts at or before the last one ends, they overlap.
        if current_start <= last_end:
            # Merge the current interval by extending the end of the last one 
            # to the maximum of the two end times.
            merged[-1] = (merged[-1][0], max(last_end, current_end))
        else:
            # If no overlap, append the current interval as a new, non-overlapping range.
            merged.append((current_start, current_end))

    return merged

if __name__ == '__main__':
    main()
 