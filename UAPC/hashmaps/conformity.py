N = int(input())

coursedict = {}
highest = 0

for _ in range(N):
    courses = tuple(sorted(map(int, input().split())))

    if courses not in coursedict:
        coursedict[courses] = 1
    else:
        coursedict[courses] += 1

    if coursedict[courses] > highest:
        highest = coursedict[courses]

ans = 0
for v in coursedict.values():
    if v == highest:
        ans += v

print(ans)