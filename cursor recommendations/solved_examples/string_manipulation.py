"""
String Manipulation Examples
Common string problems in Division 2 contests
"""

from typing import List

# Example 1: Check if string is palindrome
def is_palindrome(s: str) -> bool:
    """Check if string is palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example 2: Find longest common prefix
def longest_common_prefix(strs: List[str]) -> str:
    """Find longest common prefix among strings"""
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example 3: Count substring occurrences
def count_substring(s: str, sub: str) -> int:
    """Count occurrences of substring"""
    count = 0
    start = 0
    while True:
        pos = s.find(sub, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count

# Example 4: String anagram check
def are_anagrams(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams"""
    from collections import Counter
    return Counter(s1) == Counter(s2)

# Example 5: Reverse words in string
def reverse_words(s: str) -> str:
    """Reverse order of words in string"""
    words = s.split()
    return " ".join(reversed(words))

# Example 6: Valid parentheses
def valid_parentheses(s: str) -> bool:
    """Check if parentheses are valid"""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

# Example 7: Character frequency
def char_frequency(s: str) -> dict:
    """Count frequency of each character"""
    from collections import Counter
    return dict(Counter(s))

# Example 8: Remove duplicates while preserving order
def remove_duplicates(s: str) -> str:
    """Remove duplicate characters while preserving order"""
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

