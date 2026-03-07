"""
Standard I/O Template for Kattis Problems
Use this as a starting point for most problems
"""

import sys
from typing import List, Tuple

# Fast I/O (use when input is large)
def readints():
    return list(map(int, sys.stdin.readline().split()))

def readint():
    return int(sys.stdin.readline())

def readstr():
    return sys.stdin.readline().strip()

def readstrs():
    return sys.stdin.readline().split()

# Standard I/O (use for most problems)
def main():
    # Example: Read n integers
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Example: Read n lines
    # for _ in range(n):
    #     line = input().strip()
    
    # Example: Read until EOF
    # for line in sys.stdin:
    #     process(line)
    
    # Your solution here
    result = solve(arr)
    
    # Output
    print(result)

def solve(arr: List[int]) -> int:
    # Your algorithm here
    return sum(arr)

if __name__ == "__main__":
    main()

