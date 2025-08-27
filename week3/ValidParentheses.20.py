'''
i: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
o: whether is Valid or not

to be valid:
1) bracket has to be closed by the same type of bracket
2) open brackets needs to be closed in the correct order
3) Every closing bracket has a correspondent opening bracket

examples:
Input: s = "()[]{}"
True

Input: s = "([])"
True

Input: s = "([)]"
False

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closing_brackets = {')': '(',
                            ']': '[',
                            '}': '{'}

        for b in s:
            if b in ('(', '[', '{'):
                stack.append(b)
            else:
                if not stack or stack[-1] != closing_brackets.get(b):
                    return False
                stack.pop()
            
        if stack:
            return False
        
        return True