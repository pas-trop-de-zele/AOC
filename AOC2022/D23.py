import sys
from math import *
from pprint import pprint as pprint
import time
from sympy.ntheory.modular import crt
import heapq
from copy import *
from collections import *
import functools
from itertools import *
from math import sqrt, ceil
import threading
import cmath  
import itertools
sys.setrecursionlimit(100000)
fin = sys.stdin.read().strip().split("\n")
elfs = set()
left, top = inf, inf
right, bot = -inf, -inf
for r in range(len(fin)):
    for c in range(len(fin[0])):
        if fin[r][c] == '#':
            elfs.add((r, c))
            left = min(left, c)
            right = max(right, c)
            top = min(top, r)
            bot = max(bot, r)
def debM():
    global left, top, right, bot
    for r in range(top, bot + 1):
        for c in range(left, right + 1):
            if (r,c) in elfs:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]

"""
            [-1, 0], 
    [-1, -1]         [-1, 1],
[0, -1],                       [0, 1], 
    [1, -1]            [1, 1],        
            [1, 0]
"""

N = [[-1, -1],[-1, 0],[-1, 1]]
S = [[1, -1], [1, 0], [1, 1]]
W = [[-1, -1], [0, -1], [1, -1] ]
E = [[-1, 1],[0, 1], [1, 1],]
MOVES_ADJACENT = [[-1, 0], [1, 0], [0, -1], [0, 1]]

start = 0
def consider(r, c):
    global start
    i = start
    directions = [N,S,W,E]
    for _ in range(4):    
        there_is_elfs = False
        for dy, dx in directions[i]:
            if (r + dy, c + dx)  in elfs:
                there_is_elfs = True
                break
        if not there_is_elfs:
            ret = (r + MOVES_ADJACENT[i][0], c + MOVES_ADJACENT[i][1])
            # print(r, c, "PROPOSED", ret)
            return ret
        i = (i + 1) % 4



for round in range(1, 10000000000000000):
    # print(round)
    new = set()
    is_changed = False
    proposed = defaultdict(list)
    # part 1 look around get elfs that are surrounded
    for r, c in elfs:
        is_surrounded = False
        for dy, dx in MOVES_ALL:
            rr = r + dy
            cc = c + dx
            if (rr, cc) in elfs:
                is_surrounded = True
                break
        
        if is_surrounded:
            move = consider(r, c)
            # map each proposed move to the elfs
            if not move:
                new.add((r, c))
                continue
            proposed[move].append((r, c))
        else:
            # this elfs stay the same
            new.add((r, c))

    for next_pos, proposed_elfs in proposed.items():
        if next_pos is None:
            continue
        if len(proposed_elfs) == 1:
            # print("MOVE", proposed_elfs[0], "to", next_pos)
            new.add(next_pos)
            rr, cc = next_pos
            left = min(left, cc)
            right = max(right, cc)
            top = min(top, rr)
            bot = max(bot, rr)
            is_changed = True
        else:
            for conflicted_elf in proposed_elfs:
                new.add(conflicted_elf)

    elfs = new
    start = (start + 1) % 4
    # debM()
    if not is_changed:
        print(round, "NOT")
        assert is_changed == True

ret = 0
for r in range(top, bot + 1):
    for c in range(left, right + 1):
        if (r,c) not in elfs:
            ret += 1
print(ret)