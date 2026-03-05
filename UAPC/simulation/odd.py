N = int(input())
odd = []
for i in range(N):
    G = int(input())
    guests = list(map(int, input().split()))
    curr_dict = {}
    lol = 0
    for j in guests:
        if j not in curr_dict:
            curr_dict[j] = 1
            lol += j
        else:
            lol -= j
    odd.append(lol)

for k in range(len(odd)):
    print(f"Case #{k+1}: {odd[k]}")