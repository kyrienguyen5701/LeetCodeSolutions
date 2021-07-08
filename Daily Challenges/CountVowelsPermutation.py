'''
'''

from collections import deque

def countVowelPermutation(self, n):
    mod = 1000000007
    j = 4
    x = deque([5, 10, 19, 35])
    while j < n:
        x.append((x[3] + 2*x[2] - x[1] + x[0]) % mod)
        x.popleft()
        j += 1
    return x[n - 1] if n < 5 else x[-1]

'''
Runtime: 88ms - 98.20%
Memory Usage: 14MB - 99.23%
'''

'''
Comment: https://leetcode.com/discuss/explore/july-leetcoding-challenge-2021/1315768/Count-Vowels-Permutation-or-Math-%2B-Bottom-up-DP-w-Explanation
'''