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

fin = sys.stdin.read().strip().split("\n")
ret = 0
mx = 0

for line_id, line in enumerate(fin):
    print("ID", line_id)
    s, nums = line.split()
    nums = [int(c) for c in nums.split(',')]
    s = s + '?' + s + '?' + s + '?' + s + '?' + s
    new_nums = list(nums)
    for _ in range(4):
        new_nums.extend(nums)
    nums = list(new_nums)
    questions_index = []
    for i, c in enumerate(s):
        if c == '?':
            questions_index.append(i)
    mx = max(mx, len(questions_index) * 5)
    @functools.lru_cache(None)
    def f(cur, i, j):
        # print(cur, i, j, s[i], len(s))
        if i >= len(s):
            if j >= len(nums):
                return 1
            return 0
        
        if j >= len(nums):
            return all(s[right] != '#' for right in range(i, len(s)))
        
        if s[i] == '.':
            if cur > 0:
                # case when we already have a group but terminate early
                return 0
            # if no group then ok to move on
            return f(0, i + 1, j)
        
        if s[i] == '#':
            while i < len(s) and s[i] == '#':
                i += 1
                cur += 1
            if cur > nums[j]:
                return 0
            elif cur == nums[j]:
                return f(0, i + 1, j+1)
            else:
                return f(cur, i, j)
            
        if s[i] == '?':
            ret = 0
            if cur == 0:
                ret += f(cur, i+1, j)

            if cur + 1 == nums[j]:
                if i + 1 < len(s) and s[i+1] == '#':
                    ret += 0
                else:
                    ret += f(0, i+2, j+1)
            elif cur + 1 < nums[j]:
                ret += f(cur + 1, i+1, j)
            return ret
        return 0 

    ret += f(0, 0, 0)
    print(f(0, 0, 0))
print(ret)