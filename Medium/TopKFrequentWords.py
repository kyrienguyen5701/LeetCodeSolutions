'''
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.
'''

from collections import defaultdict
from heapq import *

def topKFrequent(words, k):
    freq = defaultdict()
    for i in range(len(words)):
        freq[words[i]] = freq.get(words[i], 0) - 1
    
    freq_list = zip(freq.values(),freq.keys())
    
    h = []
    for i in freq_list:
        heappush(h, i)

    result = []
    for i in range(k):
        t = heappop(h)
        result.append(t[1])
    
    return result

'''
Runtime: 48ms - 95.25%
Memory: 14.2MB - 80.56%
'''