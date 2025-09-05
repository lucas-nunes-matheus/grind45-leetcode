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
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        answer = [0]*len(nums)

        prefix[0] = 1
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            prefix[i] = product

        suffix[-1] = 1 
        product = 1
        for j in range(len(nums)-2, -1, -1):
            product *= nums[j+1]
            suffix[j] = product

        answer[0], answer[-1] = suffix[0], prefix[-1]

        for k in range(1, len(nums)-1):
            answer[k] = prefix[k]*suffix[k]

        return answer
        
s = Solution()
print(f"Test Case 1: nums = [1,2,3,4].\n{s.productExceptSelf([1,2,3,4]) == [24,12,8,6]}")
