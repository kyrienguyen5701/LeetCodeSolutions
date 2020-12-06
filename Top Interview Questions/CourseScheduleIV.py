'''
'''

from collections import defaultdict

def checkIfPrerequisite(n, prerequisites, queries):
    courses = defaultdict(list)
    for prerequisite in prerequisites:
        courses[prerequisite[1]].append(prerequisite[0])

    cache = dict()
    def helper(query):
        query = tuple(query)
        if query in cache.keys():
            return cache[query]
        if query[0] in courses[query[1]]:
            return True
        else:
            for prerequisite in courses[query[1]]:
                pseudo_query = (query[0], prerequisite)
                if helper(pseudo_query):
                    cache[pseudo_query] = True
                    return True
            cache[query] = False
            return False
    
    results = []
    for query in queries:
        results.append(helper(query))
    
    return results

'''
Runtime: 1236ms - 53.22%
Memory: 18.4MB - 15.88%
'''