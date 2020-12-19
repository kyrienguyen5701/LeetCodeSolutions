'''
Given an integer array nums, find the contiguous subarray(containing
at least one number) which has the largest sum and return its sum.
'''

def maxSubArray(nums):
    result = None
    i = 0
    while i < len(nums):
        if nums[i] < 0: 
            i += 1
        else:
            break
    if i == len(nums):
        return max(nums)
    result = nums[i]
    i += 1
    current = result
    while i < len(nums):
        if nums[i] >= 0 and current < 0:
            current = nums[i]
        else:
            current += nums[i]
            if current > result:
                result = current
        i += 1
    return result

'''
Runtime: 60ms - 85.38%
Memory: 14.8MB - 80.10%
'''
