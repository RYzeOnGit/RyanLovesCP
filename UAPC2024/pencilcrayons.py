N, K = map(int, input().split())
remove = 0
for _ in range(N):
    box = list(input().split())
    visited = {}
    for i in box:
        if i not in visited:
            visited[i] = 1
        else:
            remove += 1
print(remove)