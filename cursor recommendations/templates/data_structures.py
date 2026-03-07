"""
Data Structures Template
Common data structures for competitive programming
"""

from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from typing import List, Dict, Set

# Priority Queue (Min Heap)
class PriorityQueue:
    """Min heap implementation"""
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        heappush(self.heap, item)
    
    def pop(self):
        return heappop(self.heap)
    
    def peek(self):
        return self.heap[0]
    
    def empty(self):
        return len(self.heap) == 0

# Max Heap (using negative values)
class MaxHeap:
    """Max heap using negative values"""
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        heappush(self.heap, -item)
    
    def pop(self):
        return -heappop(self.heap)
    
    def peek(self):
        return -self.heap[0]
    
    def empty(self):
        return len(self.heap) == 0

# Union-Find (Disjoint Set Union)
class UnionFind:
    """Union-Find data structure for connected components"""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x: int) -> int:
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """Union two sets, returns True if merged"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        """Check if two elements are in same set"""
        return self.find(x) == self.find(y)

# Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    """Trie data structure for string operations"""
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Segment Tree (Range Sum Query)
class SegmentTree:
    """Segment tree for range queries"""
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        
        # Build tree
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, index: int, value: int):
        """Update value at index"""
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
    
    def query(self, left: int, right: int) -> int:
        """Query sum in range [left, right)"""
        left += self.size
        right += self.size
        result = 0
        
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        
        return result

# Useful collections shortcuts
def use_counter(arr: List[int]) -> Dict[int, int]:
    """Count frequency of elements"""
    return Counter(arr)

def use_defaultdict():
    """Default dict with list/set/int"""
    # List default
    d = defaultdict(list)
    d['key'].append('value')
    
    # Set default
    d = defaultdict(set)
    d['key'].add('value')
    
    # Int default
    d = defaultdict(int)
    d['key'] += 1

