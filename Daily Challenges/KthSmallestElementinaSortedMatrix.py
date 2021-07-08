'''
Given an n x n matrix where each of the rows and columns are sorted in ascending order,
return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''

def kthSmallest(self, matrix, k):
    straighten = []
    while len(matrix) > 0:
        straighten += matrix.pop()
    straighten.sort()
    return straighten[k - 1]

'''
Runtime: 164ms - 86.92%
Memory Usage: 18.3MB - 100%
'''