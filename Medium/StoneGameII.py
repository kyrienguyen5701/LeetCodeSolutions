'''
Alice and Bob continue their games with piles of stones.
There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, 
where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
'''

from functools import lru_cache
from itertools import accumulate

def stoneGameII(piles):
    n = len(piles)
    a = [*accumulate(piles[::-1])][::-1]

    @lru_cache(None)
    def game(i, m):
        if i + 2 * m >= n:
            return a[i]
        BobMin = float('inf')
        for j in range(1, 2 * m + 1):
            score = game(i + j, max([j, m]))
            BobMin = min(score, BobMin)
        return a[i] - BobMin
    return game(0, 1)

'''
Runtime: 184ms - 84.18%
Memory usage: 15.6MB - 64.76%
'''