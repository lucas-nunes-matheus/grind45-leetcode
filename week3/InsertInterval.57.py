'''
I: You are given an array of non-overlapping intervals [start_i, end_i]
O: Insert newInterval while keeping ascending order by start_i 
and without overlapping intervals

examples: 
intervals = [[1,3],[6,9]], newInterval = [2,5]
[[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
[[1,2],[3,10],[12,16]]

Constraints:
- intervals could be null? Yes.
- 0 <= intervals.length <intervals = [[1,3],[6,9]], newInterval = [2,5]= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5

Approach:
intervals = [[1,3],[6,9]], newInterval = [2,5]

'''
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        # We add the newInterval to the original intervals list
        # And we sort by the first element on them
        intervals.append(newInterval).sort()

        # We assign a res list variable to store the final non-overlapping list result
        res = [intervals[0]]

        # Iterating over the intervals list, starting from the second list
        for i in range (1, len(intervals)):
            # If the upper bound of res' last list is greater than intervals start index
            # It means the cur interval is overlapping the last res list
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            # If the upper bound of the last list on res does not cover 
            # the start index of the current interval, just append the cur interval 
            else:
                res.append(intervals[i])

        return res



        