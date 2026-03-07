"""
Quick Reference - Copy-paste snippets for common operations
Use these in your contest solutions
"""

from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys

# ===== I/O =====
# Fast input
def readints():
    return list(map(int, sys.stdin.readline().split()))

def readint():
    return int(sys.stdin.readline())

def readstr():
    return sys.stdin.readline().strip()

# ===== Graph =====
# Build undirected graph
graph = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS shortest path
def bfs_shortest(start, target):
    queue = deque([start])
    visited = {start}
    dist = {start: 0}
    while queue:
        node = queue.popleft()
        if node == target:
            return dist[node]
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return -1

# ===== Arrays =====
# Two pointers
left, right = 0, len(arr) - 1
while left < right:
    # Process
    left += 1
    right -= 1

# Sliding window
def sliding_window(arr, k):
    result = []
    window = deque()
    for i in range(len(arr)):
        while window and window[0] <= i - k:
            window.popleft()
        while window and arr[window[-1]] <= arr[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(arr[window[0]])
    return result

# ===== Math =====
# GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM
def lcm(a, b):
    return a * b // gcd(a, b)

# ===== Binary Search =====
# Standard binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Binary search on answer
def bs_answer(min_val, max_val, check_func):
    left, right = min_val, max_val
    result = min_val
    while left <= right:
        mid = (left + right) // 2
        if check_func(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

# ===== DP =====
# 1D DP
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = recurrence_relation(dp, i)

# 2D DP
dp = [[0] * (cols + 1) for _ in range(rows + 1)]
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        dp[i][j] = recurrence_relation(dp, i, j)

# ===== Union-Find =====
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

# ===== Priority Queue =====
# Min heap
heap = []
heappush(heap, value)
min_val = heappop(heap)

# Max heap (negate values)
heap = []
heappush(heap, -value)
max_val = -heappop(heap)

# ===== String =====
# Check palindrome
def is_palindrome(s):
    return s == s[::-1]

# Character frequency
freq = Counter(s)

# ===== Useful Collections =====
# Counter
counts = Counter(arr)

# Default dict
d = defaultdict(int)
d = defaultdict(list)
d = defaultdict(set)

# Deque (for queue/stack)
queue = deque()
queue.append(item)
item = queue.popleft()

stack = deque()
stack.append(item)
item = stack.pop()

