'''
Given an integer array nums -> return an array answer, answer[i] is the product of all elem of nums except nums[i]
Contraints:
Time complexity: O(n)
Without using division operator
2 <= nums.length <= 105
-30 <= nums[i] <= 30
answer[i] is guaranteed to fit in a 32-bit integer. -> Don't care to us, because, in Python, integers can have any size,
only restricted by the computer memory
'''

'''
nums = [1,2,3,4,5] -> total product
answer[i] = total_product / nums[i]


answer[i] = for x in (nums[:i] + nums[i+1:]): product = x*product

[1,2,3,4,5]
product_up_to_i = [1, 2, 6, 24, 120]
product_from_to_i = [120, 120, 60, 20, 5]

if in the middle
    answer[2] {from nums[2] -> 3} = prod_upto_i[:1]*prod_from_i[2+1:]
if in the corners
    1st -> from the second
    -1st (last) -> up to second last
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # We define an answer array
        answer = []
        # 1st is used to store the product of all elements from a specific index (product of prefix)
        prod_from_i = []
        # 2nd is used to store the product of all elements up to a specific index (product of suffix)
        prod_up_to_i = []

        # Adding the first elem to prefix arr 
        prod_up_to_i.append(nums[0])

        # We append the i'th elem times the i-1 th element to the prefix arr 
        for idx, val in enumerate(nums, start=1):
            prod_up_to_i.append(val*prod_up_to_i[idx-1]) # What will happen if I try to access an index that is not defined?
        
        # Adding the first element of suffix arr (last elem of nums, because we need to reverse the list)
        prod_from_i.append(nums[-1])

        # Adding the elems to suffix using the same technique
        for idx, val in enumerate(nums[::-1], start=1):
            prod_from_i.append(val*prod_from_i[idx-1])

        # But, in the end, we reverse the list
        prod_from_i.reverse()

        #  Building answer arr with the 1st elem
        answer.append(prod_from_i[0])

        # Using prefix and suffix arr's to work with O(n) time complexity 
        for i in range(1, len(nums)-1):
            answer.append(prod_up_to_i[i-1]*prod_from_i[i+1])

        # Adding the last element
        answer.append(prod_up_to_i[-1])

        return answer