def findLadders(beginWord, endWord, wordList):
    if not endWord in wordList:
        return []
    hash = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            hash[word[:i] + "*" + word[i+1:]].append(word)
    def edges(word):
        for i in range(len(word)):
            for newWord in hash[word[:i] + '*' + word[i+1:]]:
                if not newWord in visited:
                    yield newWord
    def findPath(end):
        res = []
        for curr in end:
            for parent in path[curr[0]]:
                res.append([parent] + curr)
        return res
    visited = set()
    path = defaultdict(set)
    begin = set([beginWord])
    end = set([endWord])
    forward = True
    while begin and end:
        if len(begin) > len(end):
            begin, end = end, begin
            forward = not forward
        temp = set()
        for word in begin:
            visited.add(word)
        for word in begin:
            for neighbor in edges(word):
                temp.add(neighbor)
                if forward:
                    path[neighbor].add(word)
                else:
                    path[word].add(neighbor)
        begin = temp
        if begin & end:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = findPath(res)
            return res
    return []

'''
Runtime: 32ms - 99.39%
Memory Usage: 14.5MB - 89.13%
'''

'''
Comment: I learnt 2-way BFS from this problem
'''