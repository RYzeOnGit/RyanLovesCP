n = -1
while n != 0:
    n = int(input())
    if n == 0:
        break
    names = []
    for i in range(n):
        name = input()
        names.append(name)
    names.sort(key = lambda x: x[:2])
    for j in names:
        print(j)
    print("")