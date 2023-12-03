import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from math import *

sys.setrecursionlimit(100000000)

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]

fin = sys.stdin.read().strip().split("\n")
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ret = 0
for line in fin:
    candidates = []
    for i, c in enumerate(line):
        if c.isdigit():
            candidates.append(c)
        for word in numbers:
            if line[i:].startswith(word):
                candidates.append(str(numbers.index(word)))
    ret += int(candidates[0] + candidates[-1])
print(ret)