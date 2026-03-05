# Undirected (roads both ways): Adjacency List
from collections import defaultdict
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# Directed (u → v only):
graph[u].append(v)
#A) dist array
dist = [-1]*(n+1)
dist[start] = 0
# When exploring u -> v:
dist[v] = dist[u] + 1
# dist dict
dist = {start: 0}
dist[v] = dist[u] + 1
# BFS on a graph
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs(start, graph, n):
    dist = [-1]*(n+1)
    dist[start] = 0
    q = deque([start])

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:              # not visited yet
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

# B) BFS on a grid (maze/islands/shortest path)
from collections import deque

DIR4 = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs_grid(sr, sc, grid):
    n, m = len(grid), len(grid[0])
    dist = [[-1]*m for _ in range(n)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        for dr, dc in DIR4:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                if grid[nr][nc] != '#':    # passable condition
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    return dist