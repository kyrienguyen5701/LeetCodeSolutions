'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
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