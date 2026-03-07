"""
Math Utilities Template
Common mathematical functions for competitive programming
"""

import math
from typing import List

# GCD and LCM
def gcd(a: int, b: int) -> int:
    """Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Least Common Multiple"""
    return a * b // gcd(a, b)

# Prime checking
def is_prime(n: int) -> bool:
    """Check if n is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Sieve of Eratosthenes
def sieve(n: int) -> List[bool]:
    """Returns boolean array where is_prime[i] indicates if i is prime"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return is_prime

# Get all primes up to n
def get_primes(n: int) -> List[int]:
    """Returns list of all primes up to n"""
    is_prime = sieve(n)
    return [i for i in range(n + 1) if is_prime[i]]

# Prime factorization
def prime_factors(n: int) -> List[int]:
    """Returns list of prime factors of n"""
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors

# Modular exponentiation
def mod_pow(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) % mod efficiently"""
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    
    return result

# Factorial
def factorial(n: int, mod: int = None) -> int:
    """Compute n! optionally modulo mod"""
    result = 1
    for i in range(2, n + 1):
        result *= i
        if mod:
            result %= mod
    return result

# Combinations (n choose k)
def nCr(n: int, k: int, mod: int = None) -> int:
    """Compute n choose k"""
    if k > n - k:
        k = n - k
    
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
        if mod:
            result %= mod
    
    return result

# Extended Euclidean Algorithm (for modular inverse)
def extended_gcd(a: int, b: int) -> tuple:
    """Returns (gcd, x, y) such that ax + by = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd_val, x, y

def mod_inverse(a: int, m: int) -> int:
    """Returns modular inverse of a modulo m"""
    gcd_val, x, _ = extended_gcd(a, m)
    if gcd_val != 1:
        return None  # Inverse doesn't exist
    return (x % m + m) % m

