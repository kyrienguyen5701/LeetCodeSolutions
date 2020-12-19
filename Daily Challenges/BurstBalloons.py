'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
on it represented by array nums. You are asked to burst all the balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
Find the maximum coins you can collect by bursting the balloons wisely.
'''

def maxCoins(nums):
    nums = [1] + nums + [1]
    dp = [[0]*len(nums) for i in range(len(nums))]
    
    for gap in range(2,len(nums)):
        for i in range(0,len(nums)-gap):
            j = i+gap
            for k in range(i+1,j):
                dp[i][j] = max(dp[i][j],nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])
                
    return dp[0][len(nums)-1]

'''
Runtime: 404ms - 79.24% 
Memory: 14.6MB - 66.87%
'''

'''
Comment: This problem is very challenging, as the approach is
obviously dynamic programming but my own solution was very slow
and got TLE. This solution was referenced from one of somes in
the discussions and I found it useful as it brought me a new way
of thinking in dynamic programming
'''