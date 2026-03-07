"""
Graph Problem Example
Problem: Find shortest path in unweighted graph (BFS)
Given a graph and two nodes, find shortest path between them
"""

from collections import deque, defaultdict

def solve_shortest_path():
    """
    BFS to find shortest path in unweighted graph
    """
    n, m = map(int, input().split())
    start, end = map(int, input().split())
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            # Reconstruct path
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    
    return []  # No path found

# Example: Count connected components
def count_components():
    """Count number of connected components in graph"""
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    components = 0
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1
    
    return components

# Example: Check if graph is bipartite
def is_bipartite():
    """Check if graph can be colored with 2 colors"""
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    color = {}
    
    def dfs(node, c):
        if node in color:
            return color[node] == c
        color[node] = c
        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - c):
                return False
        return True
    
    for i in range(n):
        if i not in color:
            if not dfs(i, 0):
                return False
    return True

if __name__ == "__main__":
    path = solve_shortest_path()
    print(len(path) - 1 if path else -1)  # Print distance

