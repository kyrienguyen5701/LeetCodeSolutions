'''
'''

def slidingPuzzle(board):
    ROW = 2
    COL = 3
    MAX_HAMMING_DISTANCE = 5
    directions = {
        'up': (1, 0),
        'right': (0, 1),
        'down': (-1, 0),
        'left': (0, -1)
    }
    empty_pos = None
    previous = None
    count = 0
    sum_hamming = 0
    for row in range(ROW):
        for col in range(COL):
            value = board[row][col]
            if value == 0:
                empty_pos = (row, col)
            else:
                true_row = (value - 1) // COL
                true_col = (value - 1) % COL
                sum_hamming += abs(true_row - row) + abs(true_col - col)
    while True:
        toBeMoved = None
        state = []
        for vector in directions.values():
            next_row, next_col = empty_pos[0] + vector[0], empty_pos[1] + vector[1]
            if (next_row >= 0 and next_row < ROW) and (next_col >= 0 and next_col < COL):
                value = board[next_row][next_col]
                if value != previous:
                    true_row = (value - 1) // COL
                    true_col = (value - 1) % COL
                    current_hamming_distance = abs(true_row - next_row) + abs(true_col - next_col)
                    state.append(current_hamming_distance)
                    next_hamming_distance = abs(true_row - empty_pos[0]) + abs(true_col - empty_pos[1])
                    if next_hamming_distance < current_hamming_distance:
                        toBeMoved = (next_row, next_col)
                        sum_hamming -= (current_hamming_distance - next_hamming_distance)
        if toBeMoved == None:
            if sum_hamming != 0:
                return -1
            return count
        board[toBeMoved[0]][toBeMoved[1]], board[empty_pos[0]][empty_pos[1]] = board[empty_pos[0]][empty_pos[1]], board[toBeMoved[0]][toBeMoved[1]]
        empty_pos = toBeMoved
        count += 1
        print(board)
        
print(slidingPuzzle([[3,2,4],[1,5,0]]))