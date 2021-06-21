'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.
'''

def shortestPalindrome(s):
    def isPalindrome(word, i, j):
        while i < j:
            if word[i] !=  word[j]:
                return False
            i += 1
            j -= 1
        return True
    for i in reversed(range(len(s))):
        if isPalindrome(s, 0, i):
            furthest = i + 1
            break
    return s if furthest == len(s) else s[furthest:][::-1] + s

# currently TLE