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