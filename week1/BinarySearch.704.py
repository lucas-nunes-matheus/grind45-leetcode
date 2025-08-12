class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 # We declare left, rigth pointers to delimeter the search's maximum space

        # Here, we are ensuring that left can over the right pointer
        # Therefore, it can check until if the search space is only one element
        # But, if left becames bigger than right, it means that
        # After search in the entire array, there is no element equals the target
        while l <= r:
            mid = (l + r) // 2 # We compute the arithmetic mean of the two pointers' indexes
            if nums[mid] == target: # If we found it, we return the index
                return mid
            elif nums[mid] < target: # If the mid is smaller, we can no consider the left side
                l = mid+1
            else:           # Or we can no consider the right side
                r = mid-1

        return -1   # If the algorithm arrived here, it means that left becames bigger than right
                    # Thus, there is no element target in the input array 
