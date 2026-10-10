# 128. Longest Consecutive Sequenc

# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# 1 2 3 4    | 100    | 200
# notice that each starting number has nothing to the left
# start with a set of the numbers 
# 100: has nothing to the left, count from 100, 101 does not exist maxS = 1
# 4: skip 3 exists 
# 200: nothing to the left count from 200, 201 does not exist maxS = 1
# 1: nothing to the left, count from 1, 2 exists, 3 exists, 4 exists, maxS = 4
# 3: skip
# 2: skip

def longSeq(nums):
    # seen = set(nums)

    # longest = 0
    # for n in nums:
    #     if ((n-1) in seen):
    #         # not the start, skip
    #         continue

    #     counter = 0
    #     while ((n + counter) in seen):
    #         counter+=1
    #     longest = max(longest,counter)
    # return longest
    numSet = set(nums)
    maxL = 0
    for n in numSet: # switch to numset for efficiency
        if (n-1) in numSet:
            continue
        counter = 0
        if ((n + counter) in numSet):
            counter+=1
        maxL = max(maxL, counter)
    return maxL


nums = [100,4,200,1,3,2]
print(longSeq(nums))
