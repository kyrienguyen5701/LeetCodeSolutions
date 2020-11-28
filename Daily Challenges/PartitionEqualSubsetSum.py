'''
Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal.
'''

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0: return False
    target = total // 2
    
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            if dp[target]: return True
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

'''
Runtime: 724ms - 72.18%
Memory: 14.1MB - 97.97%
'''