"""
Dynamic Programming Templates
Common DP patterns for competitive programming
"""

from typing import List
from functools import lru_cache

# 1D DP - Fibonacci style
def dp_1d(n: int) -> int:
    """Example: Fibonacci, climbing stairs"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# 2D DP - Grid problems
def dp_2d_grid(rows: int, cols: int, grid: List[List[int]]) -> int:
    """Example: Unique paths, minimum path sum"""
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]
    
    # Initialize first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Initialize first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill rest
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[rows-1][cols-1]

# Knapsack DP
def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """0/1 Knapsack problem"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],  # Don't take
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Take
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Memoization with decorator (for recursive DP)
@lru_cache(maxsize=None)
def memoized_dp(n: int) -> int:
    """Example: Recursive DP with memoization"""
    if n <= 1:
        return n
    return memoized_dp(n-1) + memoized_dp(n-2)

# Longest Common Subsequence
def lcs(s1: str, s2: str) -> int:
    """Longest Common Subsequence"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Longest Increasing Subsequence (O(n log n))
def lis(arr: List[int]) -> int:
    """Longest Increasing Subsequence using binary search"""
    tails = []
    
    for num in arr:
        # Binary search for insertion point
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)

