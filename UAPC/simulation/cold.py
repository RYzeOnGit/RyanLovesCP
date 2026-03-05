n = int(input())
temperatures = list(map(int, input().split()))
count = 0
for i in temperatures:
    if i < 0:
        count += 1
print(count)