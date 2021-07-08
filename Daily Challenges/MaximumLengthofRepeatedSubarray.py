'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
'''

# Solution 1: Bottom-up DP using table
def findLengthDPTable(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0
    return max([max(e) for e in dp])

'''
Runtime: 3428ms - 68.00%
Memory Usage: 39.4MB - 59.38%
'''

# Solution 2: Bottom-up DP using array
def findLengthDPArray(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [0] * (n + 1)
    res = 0
    for i in range(1, m + 1):
        prev = dp[0]
        for j in range(1, n + 1):
            temp = dp[j]
            dp[j] = prev + 1 if nums1[i-1] == nums2[j-1] else 0
            res = max(res, dp[j])
            prev = temp
    return res

'''
Runtime: 5032ms - 26.65%
Memory Usage: 14.3MB - 98.06%
'''

# Solution 3: Binary Search
def findLength(self, nums1, nums2):
    def check(length):
        seen = {A[i:i+length]
                for i in range(len(A) - length + 1)}
        return any(B[j:j+length] in seen
                    for j in range(len(B) - length + 1))
    A = ''.join(map(chr, nums1))
    B = ''.join(map(chr, nums2))
    l, r = 0, min(len(A), len(B)) + 1
    while l < r:
        m = r - (r - l) // 2
        if check(m):
            l = m
        else:
            h = m - 1
    return l

'''
Runtime: 140ms - 99.03%
Memory Usage: 14.8MB - 83.29%
'''