import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools

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
path = []
already = set()
lookup = defaultdict(int)
lookup['/'] = 0
for l in fin:
    print(l)
    print(path)
    tokens = l.split()
    if l[0] == '$':
        cmd = tokens[1]
        if cmd == 'cd':
            if tokens[2] == '/':
                path = ['/']
            elif tokens[2] == '..':
                path.pop()
            else:
                path.append('/' + tokens[2])
        elif cmd == 'ls':
            continue
    else:
        serial = ''.join(path)
        if tokens[0] == 'dir':
            dir = tokens[1]
            potential_path = ''.join(path + [f'/{tokens[1]}'])
            if potential_path not in lookup:
                lookup[potential_path] = 0
        else:
            file_size = int(tokens[0])
            # if (serial, file_size) in already:
            #     continue
            # already.add((serial, file_size))
            lookup[serial] += file_size
            print(file_size, serial, lookup[serial])
            for dir in lookup:
                if dir != serial and serial.find(dir) == 0:
                    print(serial, dir, serial.find(dir))
                    # if (dir, file_size) in already:
                    #     continue
                    # already.add((dir, file_size))
                    lookup[dir] += file_size
    pprint(lookup)

TOTAL = 70000000
FREE = TOTAL - lookup['/']
ret = math.inf
for size in lookup.values():
    if FREE + size >= 30000000:
        ret = min(ret, size)
print(ret)