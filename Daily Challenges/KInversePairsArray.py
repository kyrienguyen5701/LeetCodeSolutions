'''
For an integer array nums, an inverse pair is a pair of integers [i, j] where
0 <= i < j < nums.length and nums[i] > nums[j].
Given two integers n and k, return the number of different arrays consist of numbers
from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge,
return it modulo 10^9 + 7
'''

def kInversePairs(n, k):
    mod = 1000000007
    prev = [0] * (k + 1)
    prev[0] = 1
    for i in range(1, n + 1):
        curr = [0] * (k + 1)
        curr[0] = 1
        for j in range(1, k + 1):
            curr[j] += curr[j-1] + prev[j]
            if j-i >= 0:
                curr[j] -= prev[j-i]
            curr[j] %= mod
        prev = curr
    return curr[k]

'''
Runtime: 452ms - 68.49%
Memory Usage: 14.1MB - 100%
'''