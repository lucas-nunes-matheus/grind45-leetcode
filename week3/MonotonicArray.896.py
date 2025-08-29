'''
i: Given an integer array nums, 
o: Return true if the given array is monotonic, or false otherwise

definition:
monotone increasing: for all i <= j, nums[i] <= nums[j]
monotone decreasing: for all i <= j, nums[i] >= nums[j]

examples:
nums = [1,2,2,3]
true

nums = [6,5,4,4]
true

nums = [1,3,2]
false

Constraints:
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
'''

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        if nums == sorted(nums) or nums == sorted(nums, reverse=True):
            return True 
        
        return False
        
# s = Solution()
# print(s.isMonotonic([1, 2, 4, 4]))
# print(s.isMonotonic([6, 5, 4, 4]))
# print(s.isMonotonic([1, 3, 2]))
# print(s.isMonotonic([1]))
# print(s.isMonotonic([4, 4, 4, 4, 1]))


