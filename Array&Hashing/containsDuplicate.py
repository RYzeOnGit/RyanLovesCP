# Hashmap to check if the number is in the list using frequency
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                return True

        return False
print(Solution().hasDuplicate([1,2,3,1]))
# time complexity: O(n)
# space complexity: O(n)