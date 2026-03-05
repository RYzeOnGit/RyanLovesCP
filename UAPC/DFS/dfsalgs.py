def dfs(u, graph, visited):

    visited.add(u)

    for v in graph[u]:

        if v not in visited:
            dfs(v, graph, visited)
# Count components
visited = set()
components = 0

for node in graph:

    if node not in visited:
        dfs(node, graph, visited)
        components += 1
# DFS grid
DIR4 = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(r,c):

    visited.add((r,c))

    for dr,dc in DIR4:

        nr = r + dr
        nc = c + dc

        if 0<=nr<n and 0<=nc<m:
            if (nr,nc) not in visited and grid[nr][nc]=='L':
                dfs(nr,nc)
# BFS → shortest path
#DFS → explore / count components