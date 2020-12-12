'''
Given a positive integer n, generate an n x n matrix
filled with elements from 1 to n2 in spiral order.
'''

def generateMatrix(n):
    if n == 1:
        return [[1]]
    result = [[0 for _ in range(n)] for _ in range(n)]
    row, col = 0, 0
    i = 1
    direction = {
        'top': (-1, 0),
        'right': (0, 1),
        'bottom': (1, 0),
        'left': (0, - 1)
    }
    boundaries = {
        'top': 1,
        'right': n - 1,
        'bottom': n - 1,
        'left': 0
    }
    turn = {
        'top': 'right',
        'right': 'bottom',
        'bottom': 'left',
        'left': 'top'        
    }
    current_direction = 'right'
    while i <= n * n:
        result[row][col] = i
        row += direction[current_direction][0]
        col += direction[current_direction][1]
        i += 1
        if current_direction in ('left', 'right'):
            if col == boundaries[current_direction]:
                boundaries[current_direction] -= direction[current_direction][1]
                current_direction = turn[current_direction]
        else:
            if row == boundaries[current_direction]:
                boundaries[current_direction] -= direction[current_direction][0]
                current_direction = turn[current_direction]
    return result

'''
Runtime: 28ms - 84.67%
Memory: 14.3MB - 26.01%
'''