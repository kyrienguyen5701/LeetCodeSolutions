'''
We are given an array nums of positive integers, and two positive integers left and right (left <= right).
Return the number of (contiguous, non-empty) subarrays such that the value of
the maximum array element in that subarray is at least left and at most right.
'''

def numSubarrayBoundedMax(nums, left, right):
    res, small, mid = 0, 0 , 0
    for num in nums:
        if num > right:
            mid = 0
        else:
            mid += 1
            res += mid
        if num >= left:
            small = 0
        else:
            small += 1
            res -= small
    return res

'''
Runtime: 332ms - 71.70%
Memory Usage: 15.6MB - 97.43%
'''