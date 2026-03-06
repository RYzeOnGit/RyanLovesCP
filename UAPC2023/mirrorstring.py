MOD = 10**9 + 7

def solve():
    L, R = map(int, input().split())

    p5 = 1
    p2 = 1
    ans = 0

    for m in range(1, R + 1):
        if m % 2 == 1:
            p5 = (p5 * 5) % MOD
            p2 = (p2 * 2) % MOD

        if m >= L:
            ans = (ans + p5 + p2) % MOD

    print(ans)

solve()