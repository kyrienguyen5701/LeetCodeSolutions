'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence
of the array [0,3,1,6,2,2,7].
'''

def lengthOfLIS(self, nums):
    dp = []
    for num in nums:
        i = bisect.bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp)

'''
Runtime: 92ms - 78.25%
Memory Usage: 14.5MB - 75.22%
'''