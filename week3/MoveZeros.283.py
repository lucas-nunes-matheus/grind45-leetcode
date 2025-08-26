'''
Given an integer array nums, move all 0's to the end, while maintaining \\
the relative order of the non-zero elements.

Do not return anything. Updates must be done in-place.
 
Constraints:

a) 1 <= nums.length <= 10^4
b) -2^31 <= nums[i] <= 2^31 - 1

Examples:
i:  [0, 1, 0, 3, 12]
     l, r
    [1, 0, 0, 3, 12]
        l, r
    [1, 0, 0, 3, 12]
        l,    r
    [1, 3, 0, 0, 12]
        l,    r
    [1, 3, 0, 0, 12]
           l, r
    [1, 3, 0, 0, 12]
           l,     r
    [1, 3, 12, 0, 0]
           l,     r
o: [1,3,12,0,0]


i: [2, 1]
    l, r
o: [2, 1]

i: [2, 1, 0, 4]
    l, r
       l, r
          l, r
o: [2, 1, 4, 0]

o: [2, 1, 4, 0]


'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r  = 0, 1

        while r < len(nums):
            # We ensure the left is poiting to zero
            if nums[l] != 0:
                r += 1
                l += 1
                continue
            
            # We ensure the right is poiting to a non zero number
            if nums[r] == 0:
                r += 1
                continue
            
            # We swap the numbers when nums[left] == 0 and nums[right] != 0 is True
            nums[l], nums[r] = nums[r], nums[l]
            
        return

        