'''
Given an m x n matrix of positive integers representing the height 
of each unit cell in a 2D elevation map, 
compute the volume of water it is able to trap after raining.
'''

import heapq as hq
def trapRainWater(heightMap):
    m, n = len(heightMap), len(heightMap[0])
    pq = []
    visited = [[False for c in range(n)] for r in range(m)]
    MAX, water = 0, 0

    def pq_enqueue(r, c):
        if not visited[r][c]:
            hq.heappush(pq, [heightMap[r][c], r, c])

    for r in range(m):
        pq_enqueue(r, 0)
        pq_enqueue(r, n - 1)

    for c in range(1, n - 1):
        pq_enqueue(0, c)
        pq_enqueue(m - 1, c)

    while pq:
        current = hq.heappop(pq)
        h, r, c = current[0], current[1], current[2]
        visited[r][c] = True
        
        if h < MAX:
            water += MAX - h
        else:
            MAX = h        
        
        if r != 0:
            pq_enqueue(r - 1, c)
        if r != m - 1:
            pq_enqueue(r + 1, c)
        if c != 0:
            pq_enqueue(r, c - 1)
        if c != n - 1:
            pq_enqueue(r, c + 1)

    return water

'''
Runtime: 180ms - 89.28%
Memory: 15.3MB - 49.77%
'''

'''
Comment: A very interesting and practical problem
- using Math and data structure!
'''