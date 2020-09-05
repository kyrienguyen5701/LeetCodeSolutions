'''
A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible 
so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.
'''

def partitionLabels(s):
    first = {}
    indexes = []
    for i, c in enumerate(s):
        first.setdefault(c, i)
        pos = i
        while pos > first[c]:
            pos = indexes.pop()
        indexes.append(pos)
    indexes.append(len(s))
    return [indexes[i + 1] - indexes[i] for i in range(len(indexes) - 1)]

print(partitionLabels("eaaaabaaec"))

'''
Runtime: 36ms - 91.05%
Memory: 13.8MB - 64.16%
'''