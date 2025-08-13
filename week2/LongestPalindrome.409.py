# string s which consists of lowercase or uppercase letters
# Palindrome is a word that reads same forward and backward
# Letters are case sensitive, then, "Aa" is not a Palindrome

# Sample cases
# Input: s = "abccccdd"
# Output: 7

# Input: s = "a"
# Output: 1

# 1 <= s.length <= 2000

# s.length is even -> the first N nums needs to be the N last reversed numbers
# s.length is odd -> we can have a "center" unique number

# len(s) = 4 --> s = "AaaA"
# len(s) = 3 --> s = "AcA", c does not appear another time

# To verify if len(s) is even or odd
# If even, we have to check the num of letters used that appeared an even number of times
# Otherwise, if it is odd, we check the same of previously AND if there is a letter that appeared once

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        letters = {}

        for char in s:
            letters[char] = letters.get(char, 0) + 1

        max_length = 0

        for key in letters.keys():
            max_length += (letters[key] // 2) * 2

        for key in letters.keys():
            if letters.get(key) % 2 != 0: # I have a question about dict[key] or dict.get(key)
                max_length += 1
                break

        return max_length

# =====
# Tests
# =====

sol = Solution()
print("Test 1: s = \"abccccdd\"", sol.longestPalindrome("abccccdd"))
print("Test 2: s = \"a\"", sol.longestPalindrome("a"))
print("Test 3: s = \"AcA\"", sol.longestPalindrome("AcA"))