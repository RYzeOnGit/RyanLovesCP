# find two numbers that sum to X
l = 0
r = n-1

while l < r:

    s = arr[l] + arr[r]

    if s == target:
        print("found")
        break

    elif s < target:
        l += 1

    else:
        r -= 1

# find two numbers that sum to X
l = 0

for r in range(n):

    while condition_bad:
        l += 1

# prefix sum
prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

sum_lr = prefix[r+1] - prefix[l]

# binary search
lo, hi = 0, 10**18

while lo < hi:
    mid = (lo + hi)//2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1