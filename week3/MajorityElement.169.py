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

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        majority_element = nums[0]
        most_frequent = float("-inf")

        for key, val in counter.items():
            if val > most_frequent:
                most_frequent = val
                majority_element = key

        return majority_element