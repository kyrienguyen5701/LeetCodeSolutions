'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.
'''

from collections import Counter
def fourSumCount(A, B, C, D):
    sums = Counter(c+d for c in C for d in D)
    return sum(sums.get(-(a+b), 0) for a in A for b in B)

'''
Runtime: 228ms - 98.63%
Memory: 35MB - 71.78%
'''