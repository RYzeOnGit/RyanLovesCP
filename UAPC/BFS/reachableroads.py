from collections import deque

t = int(input())

for _ in range(t):
    m = int(input())
    r = int(input())

    adj = [[] for _ in range(m)]
    for _ in range(r):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * m
    components = 0

    for start in range(m):
        if visited[start]:
            continue
        components += 1
        q = deque([start])
        visited[start] = True

        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

    # Minimum roads needed to connect k components is k-1
    print(components - 1)