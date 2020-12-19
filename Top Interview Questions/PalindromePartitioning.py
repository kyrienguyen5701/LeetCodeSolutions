'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
'''

def partition(s):
    result = []
        
    def gather(arr, S):
        if S:
            for i in range(1, len(S) + 1):
                if S[:i] == S[:i][::-1]:
                    gather(arr + [S[:i]], S[i:])
        elif arr:
            result.append(arr)
            
    gather([], s)
    return result

'''
Runtime: 72ms - 76.71%
Memory: 14.5MB - 59.51%
'''