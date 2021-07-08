'''
Given an array arr.  You can choose a set of integers and
remove all the occurrences of these integers in the array.
Return the minimum size of the set so that at least half
of the integers of the array are removed.
'''
from collections import defaultdict

def minSetSize(self, arr):
    target = (len(arr) + 1) // 2
    freq = defaultdict(int)
    for i in arr:
        freq[i] += 1
    freq = sorted(freq.values())
    count = 0
    while target > 0:
        target -= freq.pop()
        count += 1
    return count

'''
Runtime: 568ms - 82.26%
Memory Usage: 30.5MB - 94.55%
'''