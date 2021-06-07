'''
An encoded string S is given. To find and write the decoded string to a tape,
the encoded string is read one character at a time and the following steps are taken:
If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.
'''

def decodeAtIndex(self, S, K):
    size = 0
    
    for c in S:
        if c.isdigit():
            size *= int(c)
        else:
            size += 1
    
    for c in reversed(S):
        K %= size
        
        if K == 0 and not c.isdigit():
            return c
        
        if c.isdigit():
            size //= int(c)
        else:
            size -= 1

'''
Runtime: 28ms - 75.61%
Memory: 14.2MB - 42.68%
'''