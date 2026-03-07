"""
Graph Algorithms Template
Common graph operations for competitive programming
"""

from collections import deque, defaultdict
from typing import List, Dict, Set

# Graph representation: adjacency list
graph: Dict[int, List[int]] = defaultdict(list)

def add_edge(u: int, v: int, directed: bool = False):
    """Add an edge to the graph"""
    graph[u].append(v)
    if not directed:
        graph[v].append(u)

# BFS - Shortest path in unweighted graph
def bfs(start: int, target: int) -> int:
    """Returns shortest distance from start to target, -1 if unreachable"""
    queue = deque([start])
    visited = {start}
    distance = {start: 0}
    
    while queue:
        node = queue.popleft()
        
        if node == target:
            return distance[node]
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    return -1

# DFS - Check connectivity, find cycles, etc.
def dfs(start: int, visited: Set[int] = None) -> Set[int]:
    """Returns set of all reachable nodes from start"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    
    return visited

# DFS iterative version (avoids recursion limit)
def dfs_iterative(start: int) -> Set[int]:
    """Iterative DFS to avoid recursion limits"""
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited

# Count connected components
def count_components(n: int) -> int:
    """Count number of connected components in graph with n nodes"""
    visited = set()
    components = 0
    
    for i in range(n):
        if i not in visited:
            dfs(i, visited)
            components += 1
    
    return components

# Example usage
if __name__ == "__main__":
    # Build graph
    n, m = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        add_edge(u, v)
    
    # Find shortest path
    result = bfs(0, n-1)
    print(result)

