class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Constrains:
        # The same length - OK
        # The same number of each letter - OK

        # We count the length of both strings
        length = len(s)

        # If the lengths are different, we return False
        if length != len(t):
            return False

        # We assign a dict in order to map every occurence of each letter
        letters = {}
        # We iterate by the first string and map its dif letters as keys \
        # and the ocurrences of each on such as its values
        for i in range(length):
            if letters.get(s[i]) is None:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1

        # At this step, we're gonna check if the mapped letters are exclusive enough \
        # to build the 2nd string
        for j in range(length):
            if letters.get(t[j]) is None:
                return False
            if letters.get(t[j]) > 0:
                letters[t[j]] -= 1

        # If (empty dict) returns False, then, we check if the dict is properly empty
        for l in letters.values():
            if l != 0:
                return False

        # Otherwise, the both words has the same length and number of occurences of each letter
        return True

        # Complexities:
        # - Time: O(n)
        # - Memory: O(26) -> (1) # O(26), 'cause there are at most 26 different keys