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
        prefix = [nums[i] * nums[i-1] for i in range(1, len(nums))]
        suffix = [nums[j] * nums[j+1] for j in range(len(nums)-2, -1, -1)]

        answer = [0]*len(nums)
        answer[0] = suffix[1]
        answer[-1] = prefix[-2]

        # answer = [prefix[k-1:k] * suffix[k+1:k+2] for k in range(len(nums))]
        for k in range(1, len(nums)-1):
            answer[k] = prefix[k-1] * suffix[k+1]


        return answer
        
s = Solution()
print(f"Test Case 1: nums = [1,2,3,4].\n{s.productExceptSelf([1,2,3,4]) == [24,12,8,6]}")
