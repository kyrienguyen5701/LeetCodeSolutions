'''
Given a non-empty string check if it can be constructed 
by taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only 
and its length will not exceed 10000.
'''

def repeatedSubstringPattern(s):
    dupe = s + s
    for i in range(1, len(s)):
        if dupe[i:(i + len(s))] == s:
            return True
    return False

print(repeatedSubstringPattern('abcab'))

'''
Runtime: 136ms - 42.51%
Memory: 13.9MB - 44.08%
'''