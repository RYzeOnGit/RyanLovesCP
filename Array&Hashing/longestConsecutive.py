# Time complexity: O(n)
# Space complexity: O(n)
# How we solve it:
# 1. We create a set of the numbers
# 2. We then iterate through the set and check if the number is the start of a sequence
# 3. If it is, we then check if the number plus the length is in the set
# 4. If it is, we then increment the length
# 5. We then return the longest length
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            # Check if its the start of a sequence
            if (n - 1) not in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                longest = max(length, longest)
        
        # This must be outside the for loop
        return longest