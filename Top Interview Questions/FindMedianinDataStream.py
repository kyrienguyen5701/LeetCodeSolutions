'''
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.
For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
- void addNum(int num) - Add a integer number from the data stream to the data structure.
- double findMedian() - Return the median of all elements so far.
'''

from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num):
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        

    def findMedian(self):
        has_even_count = len(self.max_heap) == len(self.min_heap)

        if has_even_count:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return float(self.min_heap[0])

'''
Runtime: 176ms - 97.54%
Memory: 25.4MB - 48.43%
'''