'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.
'''

def rob(self, nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    curr = [nums[0], max(nums[:2])]
    for i in range(2, n):
        curr[0], curr[1] = curr[1], max([nums[i] + curr[0], curr[1]])
    return curr[1]

'''
Runtime: 28ms - 87.21%
Memory Usage: 14.1MB - 92.31%
'''