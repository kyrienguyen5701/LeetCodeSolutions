'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(self, s):
    if not s:
        return 0
    result = 1
    i = 1
    checkpoints = {
        s[0]: 0
    }
    start = 0
    for i in range(1, len(s)):
        if s[i] in checkpoints.keys():
            result = max([result, i - start])
            start = max([checkpoints[s[i]] + 1, start])
        checkpoints[s[i]] = i
        if i == len(s) - 1:
            result = max([result, len(s) - start])
    return result

'''
Runtime: 56ms - 79.73%
Memory: 14.3MB - 59.12%
'''