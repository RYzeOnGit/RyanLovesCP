from collections import deque

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
q = deque([(0, 0)])
dist[0][0] = 0

while q:
    x, y = q.popleft()
    k = ord(grid[x][y]) - ord('0')

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx * k, y + dy * k
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

print(dist[n - 1][m - 1])