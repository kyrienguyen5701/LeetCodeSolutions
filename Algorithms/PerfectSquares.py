'''
'''

from collections import defaultdict
from math import sqrt

cache = defaultdict(int)
def numSquares(self, n):
    result = 1e5
    if n in cache.keys():
        return cache[n]
    if int(sqrt(n)) ** 2 == n:
        cache[n] = 1
        return 1
    for i in range(int(sqrt(n)), 0, - 1):
        result = min([result, 1 + self.numSquares(n - i ** 2)])
    cache[n]= result
    return result

'''
Runtime: 356ms - 76.31%
Memory: 14.6MB - 40.19%
'''