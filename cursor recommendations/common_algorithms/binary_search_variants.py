"""
Binary Search Variants
Different binary search patterns for competitive programming
"""

from typing import List, Callable

# Pattern 1: Find first occurrence
def first_occurrence(arr: List[int], target: int) -> int:
    """Find index of first occurrence of target"""
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

# Pattern 2: Find last occurrence
def last_occurrence(arr: List[int], target: int) -> int:
    """Find index of last occurrence of target"""
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

# Pattern 3: Find insertion point
def insertion_point(arr: List[int], target: int) -> int:
    """Find index where target should be inserted"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

# Pattern 4: Binary search on answer
def binary_search_answer(
    min_val: int,
    max_val: int,
    check: Callable[[int], bool]
) -> int:
    """
    Binary search on answer space
    check(x) returns True if x is valid
    Returns maximum valid value
    """
    left, right = min_val, max_val
    result = min_val
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Pattern 5: Find minimum in rotated sorted array
def find_min_rotated(arr: List[int]) -> int:
    """Find minimum element in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]

# Pattern 6: Find peak element
def find_peak(arr: List[int]) -> int:
    """Find peak element index"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# Pattern 7: Count occurrences
def count_occurrences(arr: List[int], target: int) -> int:
    """Count occurrences of target in sorted array"""
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1

# Example: Binary search on answer
def example_binary_search_answer():
    """Example: Find maximum height such that we can cut at least k pieces"""
    def can_cut(height: int) -> bool:
        pieces = sum(stick // height for stick in sticks)
        return pieces >= k
    
    sticks = [10, 15, 20, 25]
    k = 5
    result = binary_search_answer(1, max(sticks), can_cut)
    return result

