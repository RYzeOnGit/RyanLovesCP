from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)

q = deque([1])
visited[1] = True

while q:
    u = q.popleft()
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)

not_connected = []

for i in range(1, n + 1):
    if not visited[i]:
        not_connected.append(i)

if len(not_connected) == 0:
    print("Connected")
else:
    for house in not_connected:
        print(house)