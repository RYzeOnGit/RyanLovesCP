# Hashmap to group anagrams using frequency
# time complexity: O(n * m)
# space complexity: O(n * m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
        return res.values()