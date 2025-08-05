class NumArray:
    def __init__(self, nums: List[int]):
        
        n = len(nums)
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            
        self.prefix_sum = prefix_sum

    def sumRange(self, left: int, right: int) -> int:
        if len(self.prefix_sum) > 0:
            if left == 0:
                return self.prefix_sum[right]
            else:
                return self.prefix_sum[right] - self.prefix_sum[left-1]
        else:
            return -1


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)