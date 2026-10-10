# Problem 5 — Course Schedule
# LeetCode 207 — Medium

# Prerequisite pair:

# [course, prerequisite]

# Example:

# [1, 0]

# means:

# take 0 before 1
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 
# 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course 
# bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Problem
# can i take all the courses required 
# the courses need to be taken in order
# [1,0][0,1] this forms a dependency (a circle) where 1 requires 0 and 0 requires 1
# so this means we are looking for a cicle in the graphs 

# i want to know if each course can be taken 
# so start at the one with no dependencies 
# and then work down the list 
# if one node cannot be found then we know a cycle exists

# 1,0 2,0 3,1 3,2
# 0 : None
# 1: 0
# 2: 0
# 3: 1,2

# start at 0 because it has none, remove the node, clean up the set
# 1 and 2: None, remove the node, clean up the set 
# 3: None, remove the node, set is all none we have nothing left 
# true

from collections import defaultdict, deque

def canFinish(numCourses,prereqs):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    taken = 0
    #form graphs and indegree counts 
    for course, prereq in prereqs:
        indegree[course] +=1
        graph[prereq].append(course)

    #queue process 
    queue = deque()

    for course in range(numCourses):
        if indegree[course] == 0:
            queue.append(course)

    # BFS 

    while (queue):
        n = queue.popleft()
        taken+=1
        for neighbor in graph[n]:
            indegree[neighbor] -=1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return taken == numCourses
print(canFinish(2,[[1, 0]]))


