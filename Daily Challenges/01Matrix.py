'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
'''

from collections import deque

def updateMatrix(mat):
    checked = []
    row, col = len(mat), len(mat[0])
    for i in range(row):
        for j in range(col):
            if mat[i][j] != 0:
                checked.append([i, j])
    dist = 1
    while checked:
        new_checked = []
        for i, j in checked:
            if (i == 0 or mat[i-1][j] >= dist) \
                and (j == 0 or mat[i][j-1] >= dist) \
                and (i == row - 1 or mat[i+1][j] >= dist) \
                and (j == col - 1 or mat[i][j+1] >= dist):
                mat[i][j] = dist + 1
                new_checked.append((i,j))
        dist += 1
        checked = new_checked
                
    return mat

'''
Runtime: 460ms - 99.82%
Memory Usage: 16.8MB - 77.82%
'''