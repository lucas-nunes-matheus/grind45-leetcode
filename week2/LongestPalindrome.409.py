class Solution:
    def longestPalindrome(self, s: str) -> int:
        # a palindrome can be read the same from the right or from the left
        # it means that a palindrome word has some constraints, such as:
        # - it has to have an even number of occurences of each letter
        # - exception: in a odd length's palindrome, the center's letter can appears once
        # * important note: letters are case sensitive (then, 'A' != 'a') 
        
        letters = {}

        for l in s:
            letters[s] = letters.get(l, 0) + 1
    
        valid_letters = 0

        for k in letters.keys():
            if letters.get(k) % 2 == 0:
                valid_letters += 1

        for j in letters.keys():
            if letters.get(j) % 2 != 0:
                valid_letters += 1
                break

        return valid_letters 