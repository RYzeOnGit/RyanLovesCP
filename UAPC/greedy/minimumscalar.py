T = int(input())
ans = []
for i in range(T):
    n = int(input())
    vec1 = list(map(int, input().split()))
    vec2 = list(map(int, input().split()))
    vec1.sort()
    vec2.sort(reverse = True)
    dot = 0
    for j in range(n):
        dot += vec1[j] * vec2[j]
    ans.append(dot)
for i in range(len(ans)):
    print(f"Case #{i+1}: {ans[i]}")