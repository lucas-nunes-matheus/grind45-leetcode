'''
Subsarray is contiguos
Return -> sum (int)

1. If there is only one elem in the array -> return the elem
2. There is NO empty array as input
3. 1 <= len(nums) <= 10⁴
4. -10⁴ <= nums[i] <= 10⁴

===

Approach:
- Brute force approach is not appropiated (do not solve, I've tried)

[-2,1,-3,4,-1,2,1,-5,4] -> [4,-1,2,1]
while condition: right++;
while condition: left++;
operate;


'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 1
        cur_sum, max_sum = nums[0], nums[0]

        while cur < len(nums):
            cur_sum += nums[cur]
            if cur_sum < 0:
                cur_sum = 0

            max_sum = max(max_sum, cur_sum)
            cur += 1

        return max_sum
        