'''
You are given a 0-indexed integer array nums and an integer k.
You are initially standing at index 0. In one move, you can jump at most
k steps forward without going outside the boundaries of the array.
That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
You want to reach the last index of the array (index n - 1).
Your score is the sum of all nums[j] for each index j you visited in the array.
Return the maximum score you can get.
'''

from collections import deque

def maxResult(nums, k):
    n = len(nums)
    d = deque([n - 1])
    for i in reversed(range(n-1)):
        if d[0] - i > k:
            d.popleft()
        nums[i] += nums[d[0]]
        while len(d) and nums[d[-1]] <= nums[i]:
            d.pop()
        d.append(i)
    return nums[0]

'''
Runtime: 980ms - 91.83%
Memory Usage: 28MB - 87.34%
'''
