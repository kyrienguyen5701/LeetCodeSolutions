'''
Given an array nums, partition it into two (contiguous) subarrays left and right so that:
Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.
'''

def partitionDisjoint(self, nums):
    res, pend = 0, min(nums)
    while True:
        res += nums[res:].index(pend) + 1
        pend = min(nums[res:])
        if max(nums[:res]) <= pend:
            return res

'''
Runtime: 176ms - 92.42%
Memory Usage: 18.2MB - 91.29%
'''