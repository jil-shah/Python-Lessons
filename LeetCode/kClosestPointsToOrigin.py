# Problem 4 — K Closest Points to Origin
# LeetCode 973 — Medium
# Given an array of points where points[i] = [xi, yi] 
# represents a point on the X-Y plane and an integer k, 
# return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the 
# Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. 
# The answer is guaranteed to be unique (except for the order that it is in). 
# Point: (x, y)
# Distance from origin: sqrt(x² + y²)

# Example:

# points = [[1, 3], [-2, 2]]
# k = 1

# Squared distances:

# [1,3]   → 1^2 + 3^2 = 10
# [-2,2]  → 2^2 + 2^2 = 8

# So answer:
# [-2, 2]

# calculate the squared distance, append the (distance, point) to the heap
# heapify 
# and then remove the points
# we can use the negate to get the reverse
# Time:  O(n log k)
# Space: O(k)

import heapq

def KClosestPoints(points, k):
    heap = []
    for point in points:
        dist = point[0]*point[0]+point[1]*point[1]
        heapq.heappush(heap,(-dist, point))
        if (len(heap) > k):
            heapq.heappop(heap)

    return ([point for dist,point in heap])


points = [[1, 3], [-2, 2]]
k = 1

print(KClosestPoints(points,k))
