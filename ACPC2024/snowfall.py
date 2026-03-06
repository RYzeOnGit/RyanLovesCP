n = int(input())
snow = 0
for _ in range(n):
    t, a = map(int, input().split())
    if t == 0:
        snow += a
    if t == 1:
        if snow <= a:
            snow = 0
        else:
            snow -= a
print(snow)