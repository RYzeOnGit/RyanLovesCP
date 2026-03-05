N = int(input())
arr = []

for i in range(N):
    interval = list(map(int, input().split()))
    arr.append(interval)

best = 0
cur = -10**30

arr.sort(key=lambda x: x[1])

for a, b in arr:
    if cur < a:       # temperature doesn't fit this interval
        best += 1
        cur = b       # create room with temperature b

print(best)