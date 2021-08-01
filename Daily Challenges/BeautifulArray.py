'''
An array nums of length n is beautiful if:
nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least
one valid answer for the given n.
'''

def beautifulArray(self, n):
    def helper(nums):
        if len(nums) < 3:
            return nums
        even = nums[::2]
        odd = nums[1::2]
        return helper(even) + helper(odd)
    return helper(list(range(1, n + 1)))

'''
Runtime: 36ms - 75.54%
Memory Usage: 14.2MB - 89.21%
'''