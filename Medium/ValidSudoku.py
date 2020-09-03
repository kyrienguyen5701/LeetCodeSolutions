'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

def isValidSudoku(board):
    ROW = 9
    COL = 9
    rows = {}
    cols = {}
    boxes = {}
    box_current = 0
    
    for i in range(ROW):
        rows[i] = set()
        
        for j in range(COL):
            if(board[i][j]!="."):
                current = int(board[i][j])
                box_current = 3 * (i // 3) +  j // 3
                
                if(current in rows[i]):
                    return False
                else:
                    rows[i].add(current)
                
                if(j in cols):
                    if(current in cols[j]):
                        return False
                    cols[j].add(current)
                else:
                    cols[j] = set()
                    cols[j].add(current)
                
                if(box_current in boxes):
                    if(current in boxes[box_current]):
                        return False
                    boxes[box_current].add(current)
                else:
                    boxes[box_current] = set()
                    boxes[box_current].add(current)
    
    return True

'''
Runtime: 88ms - 99.12%
Memory: 13.6MB - 99.26%
'''