'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements
to the right of nums[i].
'''

from sortedcontainers import SortedList

def countSmaller(nums):
    n = len(nums)
    counts = [0] * n
    temp = SortedList()
    for i in reversed(range(n)):
        counts[i] = temp.bisect_left(nums[i])
        temp.add(nums[i])
    return counts

'''
Runtime: 2112ms - 91.92%
Memory Usage: 33.6MB - 66.90%
'''

'''
Comment: Nice application of merge sort
'''