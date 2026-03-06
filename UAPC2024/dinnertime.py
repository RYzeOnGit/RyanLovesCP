N = int(input())
PG = 1
P, G = 0, 0
for z in range(0, N):
    food, passing = input().split()
    passing_ = int(passing)
    if food == "G":
        Gold = G
        G += passing_
        if P > Gold:
            if P >= G:
                PG += passing_
            else:
                PG += (P - Gold)
    else:
        Pold = P
        P += passing_
        if Pold < G:
            if P >= G:
                PG += 1
print(PG)
         