'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''

def rotate(matrix):
    n = len(matrix)-1
    for i in range(n//2+1):
        for j in range((n+1)//2):
            temp = matrix[i][j]  
            matrix[i][j] = matrix[n-j][i] 
            matrix[n-j][i] = matrix[n-i][n-j] 
            matrix[n-i][n-j] = matrix[j][n-i] 
            matrix[j][n-i] = temp 

'''
Runtime: 28ms - 96.89%
Memory: 13.7MB - 84.95%
'''