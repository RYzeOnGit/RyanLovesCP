"""
Prefix Sums Template
Useful for range sum queries in O(1) time
"""

from typing import List

class PrefixSum:
    """Prefix sum array for range queries"""
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.prefix = [0] * (self.n + 1)
        
        for i in range(self.n):
            self.prefix[i + 1] = self.prefix[i] + arr[i]
    
    def query(self, left: int, right: int) -> int:
        """Get sum of range [left, right] (inclusive)"""
        return self.prefix[right + 1] - self.prefix[left]
    
    def query_range(self, left: int, right: int) -> int:
        """Get sum of range [left, right) (right exclusive)"""
        return self.prefix[right] - self.prefix[left]

# Example: 2D Prefix Sum
class PrefixSum2D:
    """2D prefix sum for matrix range queries"""
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j] +
                    self.prefix[i][j + 1] +
                    self.prefix[i + 1][j] -
                    self.prefix[i][j]
                )
    
    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """Get sum of rectangle from (r1, c1) to (r2, c2) inclusive"""
        return (
            self.prefix[r2 + 1][c2 + 1] -
            self.prefix[r1][c2 + 1] -
            self.prefix[r2 + 1][c1] +
            self.prefix[r1][c1]
        )

# Example usage
if __name__ == "__main__":
    # 1D example
    arr = [1, 2, 3, 4, 5]
    ps = PrefixSum(arr)
    print(ps.query(1, 3))  # Sum of arr[1] to arr[3] = 2+3+4 = 9
    
    # 2D example
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ps2d = PrefixSum2D(matrix)
    print(ps2d.query(0, 0, 1, 1))  # Sum of 2x2 top-left = 1+2+4+5 = 12

