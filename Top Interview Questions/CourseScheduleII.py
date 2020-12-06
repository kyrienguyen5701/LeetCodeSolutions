'''
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi]
this means you must take the course bi before the course ai. Given the total number
of courses numCourses and a list of the prerequisite pairs, return the ordering of
courses you should take to finish all courses. If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.
'''

from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    courses = {i: [] for i in range(numCourses)}
    graph = defaultdict(list)
    for prerequisite in prerequisites:
        courses[prerequisite[0]].append(prerequisite[1])
        graph[prerequisite[1]].append(prerequisite[0])
    d = deque()
    for course in courses.keys():
        if len(courses[course]) == 0:
            d.append(course)
    taken = []
    while d:
        course = d.popleft()
        taken.append(course)
        if len(taken) == numCourses:
            return taken
        for Next in graph[course]:
            Next.remove(course)
            if not courses[Next]:
                d.append(Next)
    return []

'''
Runtime:
Memory:
'''