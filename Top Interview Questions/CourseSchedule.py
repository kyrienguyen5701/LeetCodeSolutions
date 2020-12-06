
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1] Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?
'''

from collections import defaultdict

def canFinish(numCourses, prerequisites):
    schedule = defaultdict(list)
    for prerequisite in prerequisites:
        schedule[prerequisite[1]].append(prerequisite[0])
    
    def check(course, visited, rec_stack):
        visited[course] = True
        rec_stack[course] = True
        for upper in schedule[course]:
            if visited[upper] == False:
                if check(upper, visited, rec_stack) == True:
                    return True
            elif rec_stack[upper] == True:
                return True
        rec_stack[course] = False
        return False

    visited = [False] * numCourses
    rec_stack = [False] * numCourses
    for course in range(numCourses):
        if not visited[course]:
            if check(course, visited, rec_stack):
                return False
    return True

'''
Runtime: 92ms - 86.50%
Memory: 17.4MB - 11.74%
'''