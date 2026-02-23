# exactly one solution
# Checking if the complement is in the position hashmap (if it has already been seen)
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in position:
                return [position[complement], i]
            else:
                position[nums[i]] = i
        return []