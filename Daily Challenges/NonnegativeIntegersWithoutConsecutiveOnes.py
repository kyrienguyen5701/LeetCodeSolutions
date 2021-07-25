'''
Given a positive integer n, return the number of the integers in the range
[0, n] whose binary representations do not contain consecutive ones.
'''

def findIntegers(n):
    f = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 
    10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]
    res, last_seen = 1, 0
    for i in reversed(range(30)):
        add = f.pop()
        if (1 << i) & n:
            res += add
            if last_seen: 
                res -= 1
                break
            last_seen = 1
        else:
            last_seen = 0
    return res

'''
Runtime: 20ms - 100%
Memory Usage: 14MB - 98.08%
'''

