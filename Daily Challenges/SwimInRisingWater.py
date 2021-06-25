'''
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).
Now rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if and only if the elevation
of both squares individually are at most t. You can swim infinite distance in zero time.
Of course, you must stay within the boundaries of the grid during your swim.
You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?
'''

from heapq import *

def swimInWater(grid):
    n = len(grid[0])
    adjacencies = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q, heap, visited, res = [(0, 0)], [(grid[0][0], 0, 0)], {(0, 0)}, 0
    for i in range(n * n):
        val, x, y = heappop(heap)
        res = max(res, val)
        if x == n - 1 and y == n - 1:
            return res
        for dx, dy in adjacencies:
            if (x + dx, y + dy) not in visited and 0 <= x + dx < n and 0 <= y + dy < n:
                heappush(heap, (grid[x + dx][y + dy], x + dx, y + dy))
                visited.add((x + dx, y + dy))

'''
Runtime: 88ms - 98.36%
Memory Usage: 14.9MB - 63.38%
'''