import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from math import *
from dataclasses import dataclass

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
M = list(fin)
ret = 0
HEIGHT = len(M)
WIDTH = len(M[0])
parts = set()
parts_index = {}
part_cur = 0
part_val = {}
for row, s in enumerate(M):
    i = 0
    while i < WIDTH:
        if s[i].isnumeric():
            points = []
            num = ''
            j = i
            while j < WIDTH and s[j].isnumeric():
                points.append((row, j))
                num += s[j]
                j += 1
            i = j
            good = False
            for y, x in points:
                for dy, dx in MOVES_ALL:
                    yy = y+dy
                    xx = x+dx
                    if yy < 0 or yy >= HEIGHT or xx < 0 or xx >= WIDTH or M[yy][xx] == '.':
                        continue
                    if not M[yy][xx].isnumeric():
                        good = True
            if good:
                ret += int(num)
                for y,x in points:
                    parts.add((y,x))
                    parts_index[(y,x)] = part_cur
                    part_val[part_cur] = int(num)
                part_cur += 1
        else:
            i+=1

ret = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if M[y][x] == '*':
            part_index_adjavent_to = set()
            for dy, dx in MOVES_ALL:
                yy = y+dy
                xx = x+dx
                print(yy, xx)
                if yy < 0 or yy >= HEIGHT or xx < 0 or xx >= WIDTH:
                        continue
                if M[yy][xx].isnumeric():
                    if (yy,xx) in parts:
                        part_index_adjavent_to.add(parts_index[(yy,xx)])
            if len(part_index_adjavent_to) == 2:
                part_index_adjavent_to = list(part_index_adjavent_to)
                gain = part_val[part_index_adjavent_to[0]] * part_val[part_index_adjavent_to[1]]
                ret += gain
            print("="*20)
print(ret)