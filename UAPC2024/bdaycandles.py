N, H, C = map(int, input().split())
candle_dict = {}
for i in range(N):
    numbers = list(map(int, input().split()))
    numbers.sort()
    candle_dict[i] = numbers
counter = 0
index = 0
for index in range(H):
    flag = 0
    sum = 0
    number_arr = []
    for i in range(N):
        number_arr.append(candle_dict[i][index])
    number_arr.sort()
    for j in number_arr:
        if C >= j:
            C -= j
            counter += 1
        else:
            flag = 1
            break
    if flag == 1:
        break
print(counter)