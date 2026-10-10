# Problem 3 — Top K Frequent Elements
# LeetCode 347 — Medium


# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# just iterate through the list, 
# have a dictionary with the counter and add 1 for every unique element
# then we want the kth largest frequency which could be done using a heap
# so we remove the least frequency one from the list 

# Time: O(n log k) in this heap-based approach
# Space: O(n)
import heapq

def topkfreqelement(nums, k):
    freqs = {}
    for num in nums:
        if num not in freqs:
            freqs[num] = 1
        elif num in freqs:
            freqs[num] += 1

    heap = []
    # iterate through the dictionary items
    for num,freq in freqs.items():
        heapq.heappush(heap,(freq,num))
        if (len(heap) > k):
            heapq.heappop(heap)
    n = []
    for count,num in heap:
        n.append(num)
    return n

nums = [1,1,1,2,2,3]
k = 2

print(topkfreqelement(nums,k))