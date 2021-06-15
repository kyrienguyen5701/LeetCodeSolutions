'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
'''

def canJump(nums):
    furthest = 0
    i = 0
    while i < len(nums) - 1:
        if nums[i] != 0:
            furthest = max([furthest, nums[i] + i])
        else:
            if furthest == i:
                return False
        i += 1
    return True

'''
Runtime: 460ms - 44.60%
Memory Usage: 15.1MB - 99.03%
'''