'''
'''

from functools import lru_cache

@lru_cache(None)
def grayCode(self, n):
    last = 2 ** (n - 1)
    if n == 0:
        return [0]
    first_half = self.grayCode(n - 1)
    second_half = []
    for i in first_half:
        second_half.append(i + last)
    return first_half + second_half[::-1]

'''
Runtime: 92ms - 98.87%
Memory Usage: 23.1MB - 10.61%
'''