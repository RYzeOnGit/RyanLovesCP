# Hashmap to group anagrams using frequency
# time complexity: O(n * m)
# space complexity: O(n * m)
# How we solve it:
# 1. We create a hashmap to store the frequency of each character in the word
# 2. We then add the word to the hashmap with the frequency as the key
# 3. We then return the hashmap values
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
        return res.values()