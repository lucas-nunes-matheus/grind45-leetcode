'''
i: list[int] 'nums'
o: return 'answer', where answer[i] = product(nums), except nums[i]

examples:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

constraints:
- Time: O(n)
- w/o division operator
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        answer = [0]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        for j in range(len(nums)-2, -1, -1):
            suffix[j] = nums[j+1] * suffix[j+1]
        
        answer[0] = suffix[0]
        answer[-1] = prefix[-1]

        for k in range(1, len(answer)-1):
            answer[k] = prefix[k] * suffix[k]
        
        return answer
        
# s = Solution()
# print(f"Test Case 1: nums = [1,2,3,4].\n{s.productExceptSelf([1,2,3,4]) == [24,12,8,6]}")
