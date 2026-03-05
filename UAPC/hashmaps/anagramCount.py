from collections import Counter
from math import factorial

s = input().strip()

freq = Counter(s)
print(freq)
ans = factorial(len(s))

for f in freq.values():
    ans //= factorial(f)

print(ans)