'''
Given a list of unique words, return all the pairs of the distinct indices (i, j)
in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
'''

def palindromePairs(words):
    def isPalindrome(word, i, j):
        while i < j:
            if word[i] !=  word[j]:
                return False
            i += 1
            j -= 1
        return True
    wmap, res = dict(), list()
    n = len(words)
    for i in range(n):
        wmap[words[i]] = i
    for i in range(n):
        if words[i] == '':
            for j in range(n):
                if j != i and isPalindrome(words[j], 0, len(words[j]) - 1):
                    res.append([i, j])
                    res.append([j, i])
            continue
        backward = words[i][::-1]
        if backward in wmap.keys():
            pair = wmap[backward]
            if i != pair: res.append([i, pair])
        for j in range(1, len(backward)):
            if isPalindrome(backward, 0, j - 1) and backward[j:] in wmap.keys():
                res.append([i, wmap[backward[j:]]])
            if isPalindrome(backward, j, len(backward) - 1) and backward[:j] in wmap.keys():
                res.append([wmap[backward[:j]], i])
    return res

'''
Runtime: 432ms - 88.05%
Memory Usage: 15.4MB - 98.82%
'''