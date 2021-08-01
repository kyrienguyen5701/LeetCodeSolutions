'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
'''

from collections import deque

def updateMatrix(mat):
    q, visited = deque(), set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                visited.add((i,j))
                q.append((i,j))
    
    while q:
        x,y = q.popleft()
        for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
            newX, newY = x + direction[0], y + direction[1]
            if newX >= 0 and newX < len(mat) and newY >= 0 and newY < len(mat[0]) and (newX, newY) not in visited:
                    mat[newX][newY] = mat[x][y] + 1
                    visited.add((newX, newY))
                    q.append((newX, newY))
    return mat

'''
Runtime: 460ms - 99.82%
Memory Usage: 16.8MB - 77.82%
'''