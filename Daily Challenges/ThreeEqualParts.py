'''
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts
such that all of these parts represent the same binary value.
If it is possible, return any [i, j] with i + 1 < j, such that:
arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].
Note that the entire part is used when considering what binary value it represents.
For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed,
so [0,1,1] and [1,1]represent the same value.
'''

def threeEqualParts(arr):
    imp = [-1, -1]
    s = sum(arr)
    if s % 3 != 0:
        return imp
    t = s // 3
    if t == 0:
        return [0, len(arr) - 1]
    breaks = []
    count = 0
    for i, x in enumerate(arr):
        if x == 1:
            count += 1
            if count in (1, t+1, 2*t+1):
                breaks.append(i)
            if count in (t, 2*t, 3*t):
                breaks.append(i)
    i1, j1, i2, j2, i3, j3 = breaks
    if not(arr[i1:j1+1] == arr[i2:j2+1] == arr[i3:j3+1]):
        return imp
    x = i2 - j1 - 1
    y = i3 - j2 - 1
    z = len(arr) - j3 - 1
    if x < z or y < z:
        return imp
    j1 += z
    j2 += z
    return [j1, j2+1]

'''
Runtime: 372ms - 72.63%
Memory Usage: 15MB - 88.43%
'''