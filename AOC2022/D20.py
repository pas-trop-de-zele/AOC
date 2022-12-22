# import sys
# from math import *
# from pprint import pprint as pprint
# from sympy.ntheory.modular import crt
# import heapq
# from copy import *
# from collections import *
# import functools
# from itertools import *
# from math import sqrt, ceil
# import threading
# import cmath  
# import itertools
# sys.setrecursionlimit(100000)

# class Node:
#     def __init__(self, id, val, prev=None, next=None):
#         self.id = id
#         self.val = val
#         self.prev = prev
#         self.next = next

#     def __str__(self):
#         return f"Node {self.id}: {self.val}"

#     @staticmethod
#     def swap(a, b):
#         a.next = b.next
#         b.prev = a.prev
#         a.prev.next = b
#         b.next.prev = a
#         a.prev = b
#         b.next = a
#         return b, a

#     @staticmethod
#     def display(node):
#         id = node.id
#         cur = node
#         while True:
#             print(cur.val, end=' ')
#             cur = cur.next
#             if cur.id == id:
#                 break
#         print()

#     @staticmethod
#     def find_val(node, val):
#         while True:
#             if node.val == val:
#                 return node
#             node = node.next

#     @staticmethod
#     def find_id(node, id):
#         while True:
#             if node.id == id:
#                 return node
#             node = node.next

#     @staticmethod
#     def get_next(node, count):
#         ret = node
#         for _ in range(count):
#             ret = ret.next
#         return ret

# fin = sys.stdin.read().strip().split("\n")
# nums = [int(c) * 811589153 for c in fin]
# nodes = [Node(i, c) for i, c in enumerate(nums)]
# n = len(nums)
# for i in range(n):
#     prev = nodes[i-1]
#     next = nodes[i+1] if i + 1 < len(nodes) else nodes[0]
#     nodes[i].prev = prev
#     prev.next = nodes[i]
#     nodes[i].next = next
#     next.prev = nodes[i]

# HEAD = nodes[0]
# mod = n * (n - 1)
# # Node.display(HEAD)
# for round in range(10):
#     print(round)
#     for id, move in enumerate(nums):
#         print(id, move)
#         """
#         TESTING ONLY!
#         """
#         # if id > 0:
#         #     break
#         # print(id, move)
#         node = Node.find_id(HEAD, id)
#         if move == 0:
#             continue
#         elif move > 0:
#             move %= mod
#             digits = min(abs(move) + 1, n)
#             tmp = []
#             cur = node
#             for j in range(digits):
#                 if (abs(move) - j) % n == 0:
#                     tmp.append((node.id, node.val))
#                 elif abs(move) < j:
#                     tmp.append((cur.id, cur.val))
#                 else:
#                     target = ceil((abs(move) - j) / n)
#                     new_node = cur
#                     for _ in range(target):
#                         new_node = new_node.next
#                         if new_node.id == node.id:
#                             new_node = new_node.next
#                     tmp.append((new_node.id, new_node.val))
#                 cur = cur.next

#             cur = node
#             for j in range(digits):
#                 cur.id = tmp[j][0]
#                 cur.val = tmp[j][1]
#                 cur = cur.next

#         elif move < 0:
#             for _ in range(abs(move) % mod):
#                 node, _ = Node.swap(node.prev, node)
#         # Node.display(HEAD)

# zero = Node.find_val(HEAD, 0)
# ret = 0
# for _ in range(3):
#     for _ in range(1000):
#         zero = zero.next
#     ret += zero.val
# print(ret)


import sys
from math import *
from pprint import pprint as pprint
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

class Node:
    def __init__(self, id, val, prev=None, next=None):
        self.id = id
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"Node {self.id}: {self.val}"

    @staticmethod
    def swap(a, b):
        a.next = b.next
        b.prev = a.prev
        a.prev.next = b
        b.next.prev = a
        a.prev = b
        b.next = a
        return b, a

    @staticmethod
    def display(node):
        id = node.id
        cur = node
        while True:
            print(cur.val, end=' ')
            cur = cur.next
            if cur.id == id:
                break
        print()

    @staticmethod
    def find_val(node, val):
        while True:
            if node.val == val:
                return node
            node = node.next

    @staticmethod
    def find_id(node, id):
        while True:
            if node.id == id:
                return node
            node = node.next


fin = sys.stdin.read().strip().split("\n")
nums = [int(c) * 811589153 for c in fin]
nodes = [Node(i, c) for i, c in enumerate(nums)]
n = len(nums)
for i in range(n):
    prev = nodes[i-1]
    next = nodes[i+1] if i + 1 < len(nodes) else nodes[0]
    nodes[i].prev = prev
    prev.next = nodes[i]
    nodes[i].next = next
    next.prev = nodes[i]

HEAD = nodes[0]
# Node.display(HEAD)
for round in range(10):
    print(round)
    for id, move in enumerate(nums):
        """TESTING"""
        # if not id == 0:
        #     continue
        # print(id, move)
        node = Node.find_id(HEAD, id)
        if move > 0:
            for _ in range(abs(move) % (n - 1)):
                _, node = Node.swap(node, node.next)
        else:
            for _ in range(abs(move) % (n - 1)):
                node, _ = Node.swap(node.prev, node)
        # Node.display(HEAD)

zero = Node.find_val(HEAD, 0)
ret = 0
for _ in range(3):
    for _ in range(1000):
        zero = zero.next
    ret += zero.val
print(ret)