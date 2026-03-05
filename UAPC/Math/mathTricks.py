# gcd
import math
math.gcd(a, b)
lcm = a*b // math.gcd(a,b)
# instead of a^b
pow(a, b, mod)
# example
pow(2, 1000, 1000000007)
# factors
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        print(i)
        print(n//i)
# sum of first n numbers
n*(n+1)//2
# prime check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
# check power of 2
n & (n-1) == 0
# combination
import math
math.comb(n,k)
