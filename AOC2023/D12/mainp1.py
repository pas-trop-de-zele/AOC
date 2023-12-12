import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from math import *
from dataclasses import dataclass
from hashlib import md5
from itertools import permutations

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

def get_arrangement(s):
    ret = []
    i = 0
    while i < len(s):
        if s[i] == '#':
            val = 0
            j = i
            while j < len(s) and s[j] == '#':
                val += 1
                j += 1
            i = j
            ret.append(val)
        else:
            i += 1
    return tuple(ret)

fin = sys.stdin.read().strip().split("\n")
ret = 0
mx = 0
for line_id, line in enumerate(fin):
    print(line_id)
    s, nums = line.split()
    nums = [int(c) for c in nums.split(',')]
    questions_index = []
    for i, c in enumerate(s):
        if c == '?':
            questions_index.append(i)
    pattern = ''
    for i in range(1<<len(questions_index)):
        pattern = bin(i)[2:].zfill(len(questions_index))
        pattern = pattern.replace('1', '#')
        pattern = pattern.replace('0', '.')

        to_test = [c for c in s]
        for j in range(len(questions_index)):
            to_test[questions_index[j]] = pattern[j]
        to_test = ''.join(to_test)
        if tuple(get_arrangement(to_test)) == tuple(nums):
            ret += 1
print(ret)