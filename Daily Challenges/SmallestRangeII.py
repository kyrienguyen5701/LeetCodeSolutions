'''
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K,
and add x to A[i] (only once). After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the minimum value of B.
'''

def smallestRangeII(A, K):
    A.sort()
    res = float('inf')
    for i in range(len(A) - 1):
        B = [A[0] + K, A[i] + K, A[i + 1] - K, A[-1] - K]
        res = min(res, max(B) - min(B))
    return min(res, A[-1] - A[0])

'''
Runtime: 152ms - 71.76%
Memory: 15.2MB - 99.41%
'''