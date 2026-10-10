# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# count the frequency of all the numbers
# O(n) to iterate through the count
# to find the top 2, we can order the freq in order? 
# O(log n) to sort
# O(k) to get the top elements
# keep track of the topmost by using a heap
# {1:3}
#   1:3 
# 2:1 
#   1:3 
# 2:2
import heapq
def topkfreqele(nums, k):
    topk = []
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num,0)

    for n, c in count.items():
        heapq.heappush(topk,(-1*c,n)) 

    topkele = []
    for i in range(k):
        topkele.append(heapq.heappop(topk)[1])

    return topkele


nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(topkfreqele(nums,k))

# BUCKET SORT ALGORITHM
# if we have an array that keeps track of the count per index
# [1,1,1,2,2,3]
#       [0,1,2,3,4,5,6]
# 1:3   [0,0,0,1,0,0,0]
# 2:2   [0,0,2,1,0,0,0]
# 3:1   [0,3,2,1,0,0,0]
# then return topk k from the end 
# 1,2
def topkfreqele2(nums, k):
    count = {}
    # count freq of each num
    for num in nums:
        count[num] = 1 + count.get(num,0)

    freq = [[] for i in range(len(nums)+1)]
    for num,c in count.items():
        freq[c].append(num)

    res = []
    for i in range (len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
        
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(topkfreqele2(nums,k))