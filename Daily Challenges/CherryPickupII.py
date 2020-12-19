'''
Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents
the number of cherries that you can collect. You have two robots that can collect cherries for you,
Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner
(0, cols-1) of the grid. Return the maximum number of cherries collection using both robots
by following the rules below:
From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.
'''

def cherryPickup(grid):
    h, w = len(grid), len(grid[0])
    cache = {}

    def out_of_bound(col):
        return not (0 <= col < w)
    
    def optimal_pick(row, col1, col2):
        if row == h or out_of_bound(col1) or out_of_bound(col2):
            return 0
        if (row, col1, col2) in cache.keys():
            return cache[(row, col1, col2)]
        max_pick = 0
        for vec1 in (-1, 0, 1):
            for vec2 in (-1, 0, 1):
                next1, next2 = col1 + vec1, col2 + vec2
                if next1 >= next2:
                    continue
                max_pick = max(max_pick, optimal_pick(row + 1, next1, next2))
        cache[(row, col1, col2)] = max_pick + grid[row][col1] + grid[row][col2]
        return cache[(row, col1, col2)]

    return optimal_pick(0, 0, w - 1)

'''
Runtime: 1236 ms - 51.37%
Memory: 30.7 MB - 40.82%
'''