'''
i: Given an integer array 'nums'
o: Return ALL triplets [nums[i], nums[j], nums[k]] such as i != j != k, and sum of triplet == 0.

Questions:
- What is the mininum and maximum size of array nums? => [ 3 <= len(nums) <= 3000 ] 
- What is the range of possible values of nums[i]? => [ -10⁵ <= nums[i] <= 10⁵ ]

- The order of each triplets in output matters? No. Neither the order inside the triplets.
- Can output have duplicate triplets? No.

examples:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # Fix one value
        # Make the two sum proccess
        # If figure out a triplet, add to final output

        # How to add or extend lists?
        triplets = []
        # Iterating over nums
        for i in range(len(nums)):
            # Creating a new list to each number in nums
            reduced_nums = nums[:i] + nums[i+1:]

            # Assigning the target. we fixed one value, we need two others numbers which the sum will be 0
            target = 0-nums[i]

            # Two Sum solution adapted
            differences = {}
            for j in range(len(reduced_nums)):
                if differences.get(reduced_nums[j], 0) != 0:
                    if (nums[i], reduced_nums[j], reduced_nums[differences[reduced_nums[j]]]) not in triplets:
                        triplets.append((nums[i], reduced_nums[j],reduced_nums[differences[reduced_nums[j]]]))
                differences[target-reduced_nums[j]] = j
        
        triplets = list(triplets)
        return triplets
