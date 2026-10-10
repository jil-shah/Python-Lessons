# Problem 5 --- Longest Consecutive Sequence
# LeetCode 128 --- Medium
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# [100, 4, 200, 1, 3, 2]
# Longest sequence:
# 1, 2, 3, 4

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

# Brute Force: order the list of numbers, then go through the list again check if the next one is one more than the previous
# if so increase the counter, if its not 1 more, then check if the counter is more than max counter.
# if it is set it as the new max counter
# this would be O(nlogn * n)

# build a set for the numbers, this should always be unique ordered list now
# iterate through the list of numbers, if the next one higher exists add 1 and increase counter
# 1, 2, 3, 4,100,200
# 1 would get 4 
# 2 would go next get 3
# 3 -> 2
# 4 -> 1
# this is repeated work 
# so we eliminate that by only iterating from the lowest point in the sequence
# if 1 less than the curr exists dont start 

def LongestSequence(nums):
    ordered = set(nums)
    maxlength = 0
    for num in nums:
        if num-1 not in ordered:
            curr = num
            length = 1
            while (curr + 1 in ordered):
                curr += 1
                length += 1
            
            maxlength = max(length, maxlength)
    
    return maxlength


nums = [0,3,7,2,5,8,4,6,0,1]
print(LongestSequence(nums))
nums = [100, 4, 200, 1, 3, 2]
print(LongestSequence(nums))