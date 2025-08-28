'''
i: Given an array of integers nums and an integer target
o: Return indices of the two numbers that the sum of them results in target

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Examples:
i: nums = [2,7,11,15], target = 9
o: [0,1]

i: nums = [3,2,4], target = 6
o: [1,2]

i: nums = [3,3], target = 6
o: [0,1]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {}

        for idx, num in enumerate(nums):
            if diffs.get(num, None) is not None:
                return [idx, diffs.get(num)]

            diffs[target-num] = idx

        return None

