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
from copy import deepcopy
import re
import functools


GENERATED_NAMES = set()

def main():
    # # # # # # # # # # # # # # # # # # # # # #
    # --- Quest 9: Encoded in the Scales ---  #
    # # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """1:CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG
2:CTTGAATTGGGCCGTTTACCTGGTTTAACCAT
3:CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG""",
        '2': """1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG""",
        '3': """1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG
8:GGCGTAAAGTATGGATGCTGGCTAGGCACCCG""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=9, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 1
    p2 = 0
    p3 = 0

    # Part one
    ecd_data = ecd_input['1'].splitlines()
    dna = {}
    parents  = []
    child = 0
    for row in ecd_data:
        indx, d = row.split(':')
        dna[int(indx)] = d
    
    compare_list = [1, 2, 3,]
    for indx, d in dna.items():
        c = deepcopy(compare_list)
        c.remove(indx)
        for indx2, p in enumerate(d):
            if p != dna[c[0]][indx2] or p != dna[c[1]][indx2]:
                # not a child
                continue
        # if we make it here, then this is the child
        child = indx
        parents = deepcopy(c)
    
    # compare parents to child
    for parent in parents:
        parent_total = 0
        for indx, p in enumerate(dna[parent]):
            if p == dna[child][indx]:
                parent_total += 1
        p1 *= parent_total
    
    # Part two
    ecd_data = ecd_input['2'].splitlines()
    dna = {}
    children = {}
    parents = {}
    for row in ecd_data:
        indx, d = row.split(':')
        dna[int(indx)] = d
    
    for child in dna.items():
        matched = False
        for parent1 in dna.items():
            if child == parent1 or child[0] in children.keys():
                continue
            for parent2 in dna.items():
                if child == parent2 or child[0] in children.keys():
                    continue
                if compare_parents(child, parent1, parent2):
                    children[child[0]] = [parent1[0], parent2[0]]
                    if parent1[0] > parent2[0]:
                        parent1[0], parent2[0] = parent2[0], parent1[0]
                    if (parent1[0], parent2[0]) not in parents.keys():
                        parents[(parent1[0], parent2[0])] = [child[0]]
                    else:
                        parents[(parent1[0], parent2[0])].append(child[0])
                    p2 += calc_similarity(child, parent1, parent2)

    # Part three
    ecd_data = ecd_input['3'].splitlines()
    dna = {}
    children = {}
    parents = {}
    for row in ecd_data:
        indx, d = row.split(':')
        dna[int(indx)] = d
    
    for child in dna.items():
        matched = False
        for parent1 in dna.items():
            if child == parent1 or child[0] in children.keys():
                continue
            for parent2 in dna.items():
                if child == parent2 or child[0] in children.keys():
                    continue
                if compare_parents(child, parent1, parent2):
                    children[child[0]] = [parent1[0], parent2[0]]
                    if parent1[0] not in parents.keys():
                        parents[parent1[0]] = [child[0]]
                    else:
                        parents[parent1[0]].append(child[0])
                    if parent2[0] not in parents.keys():
                        parents[parent2[0]] = [child[0]]
                    else:
                        parents[parent2[0]].append(child[0])
    
    for child in children:
        if child in parents.keys():
            # This cannot be the largest try, because this duck has children
            continue
        tree_size = calc_tree_size(child, children, parents, [])
        if tree_size > p3:
            p3 = tree_size


    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

def calc_similarity(child, parent1, parent2):
    parent1_total = 0
    parent2_total = 0
    for indx, p in enumerate(child[1]):
        if p == parent1[1][indx]:
            parent1_total += 1
        if p == parent2[1][indx]:
            parent2_total += 1
    return parent1_total * parent2_total

def compare_parents(child, parent1, parent2):
    for indx, x in enumerate(child[1]):
        if x != parent1[1][indx] and x != parent2[1][indx]:
            return False
    return True

def calc_tree_size(child, children, parents, completed):
    if child in completed:
        return 0
    completed.append(child)
    ts = child
    if child in parents.keys():
        for p in parents[child]:
            ts += calc_tree_size(p, children, parents,completed)
            # completed.append(p)
    if child in children.keys():
        for c in children[child]:
            ts += calc_tree_size(c, children, parents,completed)
            # completed.append(c)
    return ts



if __name__ == '__main__':
    main()
 