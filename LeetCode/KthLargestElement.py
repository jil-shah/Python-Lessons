# Problem 1 — Kth Largest Element in a Stream
# LeetCode 703 — Easy

# Suppose:
# k = 3
# initial values = [4, 5, 8, 2]

# Given an integer array nums and an integer k, 
# return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Can you solve it without sorting?
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Since we dont care about ordering then we can store in a heap and then use the pop methodology to get the 3rd largest
# repeatedly sorting is expensive 
# technically i only need to know the 3 largest 
# since we need the smallest of the three we use the minheap
import heapq
nums = [3,2,1,5,6,4]
k = 2

# 3 - [3]
# 2 - [3,2]
# 1 - [3,2,1] -> length greater push the smallest out [3,2]
# 5 - [5,3,1] -> push smallest out [5,3]
# 6 - [6,5,3] -> [6,5]
# 4 - [4,6,5] -> [6,5]
# O(logk)
class KthLargest:
    def __init__(self,k,nums):
        self.k = k
        self.heap = nums[:]

        heapq.heapify(self.heap)

        while(len(self.heap) > k ):
            heapq.heappop(self.heap)

    def add(self,val):
        heapq.heappush(self.heap,val)
        if (len(self.heap) > self.k):
            heapq.heappop(self.heap)
        return self.heap[0]
    
k=KthLargest(k,nums)
print(k.heap[0])