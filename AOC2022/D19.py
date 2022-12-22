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

FINAL = 32
dp = {}
max_gain = 0
def f(ore_robots, clay_robots, obsidian_robots, geode_robots, ores, clays, obsidians, time, made):
    hash = (made, time)
    if hash in dp:
        return dp[hash]
    
    if time == FINAL:
        return geode_robots

    ores += ore_robots
    clays += clay_robots
    obsidians += obsidian_robots

    ret = 0
    if ores - ore_robots >= geode_robot_ore_cost and obsidians - obsidian_robots >= geode_robot_obsidian_cost:
        ret = max(ret, f(ore_robots, clay_robots, obsidian_robots, geode_robots + 1, ores - geode_robot_ore_cost, clays, obsidians - geode_robot_obsidian_cost, time + 1, made + 'G'))
    else:
        if ores - ore_robots >= obsidian_robot_ore_cost and clays - clay_robots >= obsidian_robot_clay_cost and obsidian_robots < geode_robot_obsidian_cost:
            ret = max(ret, f(ore_robots, clay_robots, obsidian_robots + 1, geode_robots, ores - obsidian_robot_ore_cost, clays - obsidian_robot_clay_cost, obsidians, time + 1, made + 'S'))

        if ores - ore_robots >= ore_robot_cost and ore_robots < max(clay_robot_cost, obsidian_robot_ore_cost, geode_robot_ore_cost):
            ret = max(ret, f(ore_robots + 1, clay_robots, obsidian_robots, geode_robots, ores - ore_robot_cost, clays, obsidians, time + 1, made + 'O'))

        if ores - ore_robots >= clay_robot_cost and clay_robots < obsidian_robot_clay_cost:
            ret = max(ret, f(ore_robots, clay_robots + 1, obsidian_robots, geode_robots, ores - clay_robot_cost, clays, obsidians, time + 1, made + 'C'))

        
        ret = max(ret, f(ore_robots, clay_robots, obsidian_robots, geode_robots, ores, clays, obsidians, time + 1, made))
        
    dp[hash] = geode_robots + ret
    return dp[hash]

ret = 1
fin = sys.stdin.read().strip().split("\n")
start = time.time()
for i, l in enumerate(fin):
    id = i + 1
    l = l.split()
    ore_robot_cost = int(l[6])
    clay_robot_cost = int(l[12])
    obsidian_robot_ore_cost = int(l[18])
    obsidian_robot_clay_cost = int(l[21])
    geode_robot_ore_cost = int(l[27])
    geode_robot_obsidian_cost = int(l[30])
    print(ore_robot_cost,clay_robot_cost, obsidian_robot_ore_cost,obsidian_robot_clay_cost,geode_robot_ore_cost,geode_robot_obsidian_cost)
    dp.clear()
    quality_level = f(1,0,0,0,0,0,0,1,'')
    print(id,":", quality_level)
    ret *= quality_level
print(ret)
end = time.time()
print("FINISHED", end - start)