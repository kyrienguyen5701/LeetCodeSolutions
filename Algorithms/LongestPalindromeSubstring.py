'''
Given a string s, return the longest palindromic substring in s.
'''

def longestPalindrome(s):
    res = ''
    def helper(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left + 1 : right]
    
    
    for index in range(len(s)):
        res = max(helper(index, index), helper(index, index + 1), res, key = len)
        
    return res

'''
Runtime: 1192ms - 53.25%
Memory Usage: 14MB - 99.93%
'''