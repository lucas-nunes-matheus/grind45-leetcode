'''
Important notes
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"   ", 3 times " " (blank space), output would be 0 or 1 ==> we'll return 0
"" as input should return 0
return LENGTH of substring, ONLY

Thinking

1. "a b c a b c b b"

    r, l
    1. while r != last element, iterate by every elem in s
    2. while the window has repeated elements, we'll move the l
    3. we store the length 

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        r, l = 0, 0
        counter = {}
        
        while r < len(s):
            counter[s[r]] = counter.get(s[r], 0) + 1
            r +=1
            while counter.get(s[r]) > 0:
                counter[s[l]] -= 1
                l +=1
            max_len = max(max_len, r-l+1)

        return max_len
