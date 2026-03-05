# check if two words are anagrams
from collections import Counter

Counter("listen") == Counter("silent")

# String Splitting / Tokenization
s = "of in the cold food"
words = s.split()

words.reverse()
print(" ".join(words))

# Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# Substring scan
if "abc" in s:
    print("found")


for i in range(len(s)-k+1):
    sub = s[i:i+k]

# Sorting Characters
key = "".join(sorted(word))