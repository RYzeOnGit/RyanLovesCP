"""
Sorting and Searching Templates
Common patterns for competitive programming
"""

from bisect import bisect_left, bisect_right
from typing import List

# Binary Search - Find first occurrence
def binary_search_first(arr: List[int], target: int) -> int:
    """Returns index of first occurrence of target, -1 if not found"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Binary Search - Find last occurrence
def binary_search_last(arr: List[int], target: int) -> int:
    """Returns index of last occurrence of target, -1 if not found"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Binary Search - Find insertion point (using bisect)
def find_insertion_point(arr: List[int], target: int) -> int:
    """Returns index where target should be inserted to maintain sorted order"""
    return bisect_left(arr, target)

# Binary Search on answer (for optimization problems)
def binary_search_answer(min_val: int, max_val: int, check_func) -> int:
    """
    Binary search on answer space
    check_func(x) returns True if x is valid, False otherwise
    Returns maximum valid value
    """
    left, right = min_val, max_val
    result = min_val
    
    while left <= right:
        mid = (left + right) // 2
        if check_func(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Custom sorting with key
def sort_by_custom_key(items: List[tuple]) -> List[tuple]:
    """Sort by multiple criteria"""
    # Sort by second element, then by first element
    return sorted(items, key=lambda x: (x[1], x[0]))

# Two pointers technique
def two_pointers(arr: List[int], target: int) -> bool:
    """Check if two elements sum to target (sorted array)"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return False

# Sliding window
def sliding_window_max(arr: List[int], k: int) -> List[int]:
    """Find maximum in each window of size k"""
    from collections import deque
    
    result = []
    dq = deque()  # Store indices
    
    for i in range(len(arr)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices with smaller values
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result

