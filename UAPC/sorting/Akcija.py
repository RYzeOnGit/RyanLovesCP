n = int(input())
prices = [int(input()) for _ in range(n)]

prices.sort(reverse=True)

total = 0

for i in range(n):
    if i % 3 != 2:  # every 3rd book is free
        total += prices[i]

print(total)