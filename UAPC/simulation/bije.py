weird = list(map(int, input().split()))
ideal = [1, 1, 2, 2, 2, 8]
for i in range(len(weird)):
    print(ideal[i] - weird[i], end=" ")