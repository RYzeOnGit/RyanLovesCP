N = int(input())
names = []
for i in range(N):
    name = input()
    names.append(name)
ascend = sorted(names)
descend = sorted(names, reverse = True)
if names == ascend:
    print("INCREASING")
elif names == descend:
    print("DECREASING")
else:
    print("NEITHER")