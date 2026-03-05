N, M = map(int, input().split())
freq = {}
highest = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        freq[i + j] = freq.get(i + j, 0) + 1
        if freq[i + j] > highest:
            highest = freq[i+j]
for f in freq.keys():
    if freq[f] == highest:
        print(f)
        