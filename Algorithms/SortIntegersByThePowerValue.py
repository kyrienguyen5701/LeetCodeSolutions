'''
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

- If x is even then x = x / 2
- If x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers low, high and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the k-th integer in the range [low, high] sorted by the power value.
'''

cache = {1: 0,2: 1,3: 7,4: 2, 5: 5, 6: 8, 7: 16, 8: 3}

def getPower(n):
    steps = 0
    rem = n % 8
    if rem == 0:
        n = n // 8
        steps = 3
    elif rem == 1:
        n = n // 8 * 9 + 2
        steps = 5
    elif rem == 2:
        n = n // 8 * 3 + 1
        steps = 4
    elif rem == 3:
        n = n // 8 * 9 + 4
        steps = 5
    elif rem == 4 or rem == 5:
        n = n // 8 * 3 + 2
        steps = 4
    elif rem == 6:
        n = n // 8 * 9 + 8
        steps = 5
    else:
        n = n // 8 * 27 + 26
        steps = 6
    if n in cache.keys(): 
        return cache[n] + steps
    else:
        return getPower(n) + steps

def getKth(low, high, k):
    data = [getPower(i) for i in range(low, high + 1)]
    sorted_data = sorted(zip(data, range(len(data))), key= lambda x:x[0])
    return sorted_data[k - 1][1] + low

'''
         Memoization     | w/o Memoization
Runtime: 512ms  - 60.86% | 412ms  - 63.43%
Memory : 13.9MB - 77.45% | 14.1MB - 42.80%
'''

'''
Comment: This problem is bad in term of constraints,
as solutions with memoization is ~100ms slower than
solutions without memoization. Also, checking a nontrivial
modulo (most solutions use modulo 2) significantly improves
the program (my first submission using modulo 2 took 1692ms) 
'''