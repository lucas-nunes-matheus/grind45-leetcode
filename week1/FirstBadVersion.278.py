# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        lo, hi = 1, n # We assign two pointers, high and low
        ans = n       # We assign a variable to store the oldest bad version currently

        while lo <= hi:             # We ensure the search space can be up to one elemente (lo <= hi) 
            mid = (lo+hi) // 2      # It was an pythonic option, but could be "lo + (hi-lo) // 2"
            if isBadVersion(mid):   
                ans = mid           # If the mid is a bad version, store its value
                hi = mid-1          # If the mid is a bad version, previously bad version can exists
            else:           
                lo = mid+1          # If the mis is not a bad version, we'll search at the right
                                    
        return ans                  # Important note: We'll never call "isBadVersion" with an invalid value
                                    # because we ever check whether lo <= hi or not before call the fn 