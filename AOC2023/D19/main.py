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
from sympy.ntheory.modular import crt 
import hashlib
from time import sleep
from enum import Enum
import json

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

def get_range_from_condition(s):
    if '>' in s:
        val = int(s[s.index('>') + 1:])
        return range(val+1, 4001)
    elif '<' in s:
        val = int(s[s.index('<') + 1:])
        return range(1, val) # range non inclusive
    assert False

def get_intersect_range(a,b):
    common = sorted(list(set(a) & set(b)))
    if common:
        return range(common[0], common[-1]+1)
    return range(0,0)

def count_permutations(ranges):
    ret = 1
    for v in ranges: 
        if len(v) == 0:
            return 0
        ret *= len(v)
    return ret

def get_opposite_range(x):
    if x[-1] != 4000: # ex: [1, 1350] range(1, 1351) x < 1351
        return range(x[-1]+1, 4001)
    else: # ex: [2441, 4000] range(2441, 4001) x > 2440
        return range(1, x[0])
    
assert get_opposite_range(range(1,1351)) == range(1351, 4001)
assert get_opposite_range(range(2441, 4001)) == range(1, 2441)

# list of tuples, 
RULES = defaultdict(list)
LAST_RESORT = {}

fin = sys.stdin.read().strip().split('\n\n')
for s in fin[0].split("\n"):
    id_ = s[:s.index('{')]
    conditions = s[s.index('{')+1:-1]
    conditions = conditions.split(",")
    # left side is always in  x,m,a,s
    for condition_id, condition in enumerate(conditions):
        if condition_id == len(conditions) - 1:
            LAST_RESORT[id_] = condition
        else:
            consider, destination = condition.split(':')
            var = consider[0]
            RULES[id_].append((var, get_range_from_condition(consider), destination))

RET = 0
STARTING_RULE = 'in'
ACCEPT = 'A'
REJECT = 'R'
def is_good(hold, cur):
    for var, valid_range, destination in RULES[cur]:
        if get_intersect_range(hold[var], valid_range):
            if destination == REJECT:
                return False
            elif destination == ACCEPT: return True
            return is_good(hold, destination)

    # last resort
    if LAST_RESORT[cur] == REJECT: 
        return False
    elif LAST_RESORT[cur] == ACCEPT: return True
    else: return is_good(hold, LAST_RESORT[cur])

def checkp1():
    ret = 0
    for id_, s in enumerate(fin[1].split("\n")):
        s = s.replace('=', ':')
        obj = json.loads(s)
        if is_good(obj, STARTING_RULE):
            ret += sum((v for v in obj.values()))
    print(ret)


good_configs = []
starting_config = {c: range(1,4001) for c in 'xmas'}
q = deque([(1, starting_config, STARTING_RULE)])
ret = 0
def cal():
    while q:
        space, cur_config, rule_id = q.popleft()
        # modify cur config over time
        for var, valid_range, destination in RULES[rule_id]:
            common = get_intersect_range(cur_config[var], valid_range)
            if common:
                if destination == ACCEPT:
                    accepted_config = dict(cur_config)
                    accepted_config[var] = common
                    
                    good_configs.append(([accepted_config[c] for c in 'xmas'], var, rule_id))
                elif destination != REJECT:
                    new_config = dict(cur_config)
                    new_config[var] = common
                    q.append((space+4,new_config, destination))
            
                # Update the range for the skip variable
                opposite_valid_range = get_opposite_range(valid_range)
                cur_config[var] = get_intersect_range(cur_config[var], opposite_valid_range)

        if LAST_RESORT[rule_id] == ACCEPT:
            good_configs.append(([cur_config[c] for c in 'xmas'], 'last resort', rule_id))
        elif LAST_RESORT[rule_id] != REJECT:
            q.append((space+4, dict(cur_config), LAST_RESORT[rule_id]))
cal()
print(sum((count_permutations(config[0]) for config in good_configs)))
