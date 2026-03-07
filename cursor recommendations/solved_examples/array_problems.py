"""
Array Problem Examples
Common array manipulation problems in Division 2
"""

from typing import List

# Example 1: Two Sum
def two_sum(nums: List[int], target: int) -> List[int]:
    """Find two indices whose values sum to target"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example 2: Maximum subarray sum (Kadane's algorithm)
def max_subarray_sum(arr: List[int]) -> int:
    """Find maximum sum of contiguous subarray"""
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example 3: Find missing number
def missing_number(n: int, arr: List[int]) -> int:
    """Find missing number in array containing 1 to n"""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example 4: Rotate array
def rotate_array(arr: List[int], k: int) -> List[int]:
    """Rotate array right by k positions"""
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# Example 5: Find duplicates
def find_duplicates(arr: List[int]) -> List[int]:
    """Find all duplicate numbers"""
    seen = set()
    duplicates = []
    for num in arr:
        if num in seen:
            duplicates.append(num)
        seen.add(num)
    return duplicates

# Example 6: Product except self
def product_except_self(nums: List[int]) -> List[int]:
    """Return array where result[i] is product of all elements except nums[i]"""
    n = len(nums)
    result = [1] * n
    
    # Left products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Right products
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result

# Example 7: Merge sorted arrays
def merge_sorted(arr1: List[int], arr2: List[int]) -> List[int]:
    """Merge two sorted arrays"""
    result = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

# Example 8: Find peak element
def find_peak(arr: List[int]) -> int:
    """Find index of peak element (greater than neighbors)"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

