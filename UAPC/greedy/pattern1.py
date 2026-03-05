arr.sort(key=lambda x: x[1])
best = 0
cur = -10**30
for a, b in arr:
    if a >= cur:
        best += 1
        cur = b
 # “Max number of non-overlapping intervals?”
 