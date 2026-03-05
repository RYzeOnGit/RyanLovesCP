from collections import deque

DIR4 = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs_grid(sr, sc, grid):

    n = len(grid)
    m = len(grid[0])

    dist = [[-1]*m for _ in range(n)]

    q = deque()
    q.append((sr, sc))

    dist[sr][sc] = 0

    while q:

        r, c = q.popleft()

        for dr, dc in DIR4:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m:

                if dist[nr][nc] == -1 and grid[nr][nc] != '#':

                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    return dist