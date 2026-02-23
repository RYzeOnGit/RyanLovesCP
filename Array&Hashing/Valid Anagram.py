# Hashmap to check if the string is an anagram using frequency
# time complexity: O(s + t)
# space complexity: O(s + t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for i in s:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        for i in t:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1

        return freq1 == freq2