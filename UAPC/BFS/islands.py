from collections import deque

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
ans = 0

for i in range(R):
    for j in range(C):
        # We only explore regions that are NOT water (i.e., 'L' or 'C')
        if visited[i][j] or grid[i][j] == 'W':
            continue

        # BFS/DFS over this non-water connected component
        q = deque([(i, j)])
        visited[i][j] = True
        has_land = (grid[i][j] == 'L')

        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] != 'W':
                    visited[nx][ny] = True
                    if grid[nx][ny] == 'L':
                        has_land = True
                    q.append((nx, ny))

        # This whole component can be made into 1 island iff it contains any forced land ('L')
        if has_land:
            ans += 1

print(ans)