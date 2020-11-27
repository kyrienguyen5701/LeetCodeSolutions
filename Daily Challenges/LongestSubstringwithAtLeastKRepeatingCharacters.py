'''
Given a string s and an integer k, return the length of the longest substring
of s such that the frequency of each character in this substring is greater than or equal to k.
'''

def longestSubstring(s, k):
    if len(s) == 0: return 0
    count = {}
    for c in s:
        try:
            count[c] += 1
        except:
            count[c] = 1
    cut = []
    for key in count.keys():
        if count[key] < k:
            cut.append(key)
    if len(cut) == 0:
        return len(s)
    candidates = []
    start = 0
    for i in range(len(s)):
        if s[i] in cut:
            candidates.append(s[start:i])
            start = i + 1
    candidates.append(s[start:])
    result = 0
    for candidate in candidates:
        if len(candidate) > 0:
            result = max([result, longestSubstring(candidate, k)])
    return result

'''
Runtime: 32ms - 83.66%
Memory: 14.3MB - 45.53%
'''
    