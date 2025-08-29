'''
i: Given an array nums of size n
o: return the majority element (elem that appears more than len(nums)/2 times) 

examples:
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Contraints:
1) You may assume that the majority element always exists in the array.
2) 1 <= len(nums) <= 5 * 10^4
3) -10^9 <= nums[i] <= 10^9
'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        counter = {}
        higher_frequency = majority_element = 0 

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
            if counter[num] > higher_frequency:
                higher_frequency = counter[num]
                majority_element = num

        return majority_element

# s = Solution()
# print(s.majorityElement([1]))
# print(s.majorityElement([3,2,3]))
# print(s.majorityElement([2,2,1,1,1,2,2]))