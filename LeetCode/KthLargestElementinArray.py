# Problem 2 — Kth Largest Element in an Array
# LeetCode 215 — Medium

# nums = [3, 2, 1, 5, 6, 4]
# k = 2

# Answer:

# 5

# same solution as befpre
# first think about sorting but then this would (nlogn)
# then use the heap methodology
import heapq
def kthLargestArray(nums,k):
    heap =[]
    for num in nums:
        heapq.heappush(heap,num)
        if (len(heap) > k):
            heapq.heappop(heap)
    return heap[0]

nums = [3, 2, 1, 5, 6, 4]
k = 2

print(kthLargestArray(nums,k))