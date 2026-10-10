# 210. Course Schedule II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi first 
# if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid 
# answers, return any of them. If it is impossible to finish all courses, return an empty array.


# Problem is that we want to find any one path that lets us complete all the courses required

# we essentially need to start at the course that requires no pre-req
# if one exists then we queue that course into the schedule 
# once we have the starting point, we deque, update the remaining courses connect, 
# and then enqueue if that course has no prereq now
# repeat until all courses are evaluated

# we need to store the order 
# we would deque any time the course can be taken so when we deque we would need to remember that it was dequeud

from collections import deque, defaultdict
def courseschedule(numCourses, prereqs):
    graph = defaultdict(list) # if 0 is not in graph
    indegree = [0] * numCourses

    # build the graphs connections, and the indegree/counter 
    for course, prereq in prereqs:
        #course -> prereq
        graph[prereq].append(course)
        indegree[course]+=1

    #queue
    queue = deque()

    for course in range(numCourses):
        if(indegree[course] == 0):
            queue.append(course)
    
    plan = []
    # dequeue and go through courses 
    while(queue):
        course = queue.popleft()
        plan.append(course)
        for neighbor in graph[course]:
            indegree[neighbor] -=1
            if (indegree[neighbor] == 0):
                queue.append(neighbor)
    return plan if len(plan) == numCourses else []

print(courseschedule(4,[[1,0],[2,0],[3,1],[3,2]]))



 