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
from itertools import permutations, combinations
from sympy.ntheory.modular import crt 
from sympy import Point3D, Line3D, symbols, solve
import hashlib
from time import sleep
from enum import Enum
import json
import copy

sys.setrecursionlimit(10000000)

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]

fin = sys.stdin.read().strip().split('\n')
stones = []
for line in fin:
    pos, vel = [x.strip() for x  in line.split('@')]
    pos = [int(c.strip()) for c in pos.split(',')]
    vel = [int(c.strip()) for c in vel.split(',')]
    stones.append((*pos, *vel))


shx,shy,shz,shvx,shvy,shvz = symbols("shx shy shz shvx shvy shvz")

"""
shx - hailstone x
shy - hailstone y
shz - hailstone z
shvx - hailstone delta x
shvy - hailstone delta y
shvz - hailstone delta z

sx + t*svx = shx + t*shvx
sx + t*svx - shx - t*shvx = 0
t*svx - t*shvx = shx - sx
t(svx - shvx) = shx - sx
t = (shx - sx) / (svx - shvx) = (shy - sy) / (svy - shvy) = (shz - sz) / (svz - shvz)
"""

equations = []
for sx,sy,sz,svx,svy,svz in stones:
    # (shx - sx) / (svx - shvx) = (shy - sy) / (svy - shvy) nhan cheo chia ngang
    equations.append((shx - sx) * (svy - shvy) - (svx - shvx) * (shy - sy))

    # (shy - sy) / (svy - shvy) = (shz - sz) / (svz - shvz) nhan cheo chia ngnang
    equations.append((shy - sy) * (svz - shvz) - (shz - sz) * (svy - shvy))

ans = solve(equations)[0]
print(ans[shx] + ans[shy] + ans[shz])