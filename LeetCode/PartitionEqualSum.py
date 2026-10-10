# 416. Partition Equal Subset Sum
# Given an integer array nums, return true if you can partition the array into two subsets 
# such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


# Problem: 
# is that we want to use integers in the array to see if we can get the target where one subset is equal to the other
# can it be in a random order? yes
# if no nums are provided is the answer false? or do we assume nums length >1
# if one num is provided, the answer is false?

# for each num we have 2 choices, include it or not - decision dp
# Brute Force: 
# we want to divide into 2 subsets that are equal which means the target is half the total
# 1+5+11+5 =22
# start with 1 we take it remaining 11-1=10
# start with 5 -> 5
# start with 11 -> not possible 
# start with 5 -> 0

# smaller problem is can i reach the remaining target with the remaining integers
# and because of this you can get repeated smaller problems
# target 3, index 3

# how to identify a repeated smaller problem 
# the target remainder and the index to test. 

# top down: dp[index,target] = can i make target using numbers from the index
# for each index we need to try taking the number or not and see if we reach target
# target - nums[index] or target 
# therefore its can i solve target or target- nums[index]

# when to stop: when target == 0, return true 
# ran out of numbers: return false 

# another solution for optimization is from bottom-up
# which means we dont try eliminating the target at each step
# we keep adding possibilities until we reach the target 
# ie we start with 1 possibilities are take it or skip it [0,1]
# 5 -> [0,1,5,6] target not in list
# 11 -> [11, 12, 16,17] target in list return 

def partitionEqualSum(nums):
    total = sum(nums)

    if (total % 2 == 1):
        return False

    target = total//2
    possible = {0}

    for num in nums:
        next_possible = possible.copy()
        for currentsum in possible:
            newsum = currentsum + num

            if newsum == target:
                return True
            elif newsum < target:
                next_possible.add(newsum)
        possible = next_possible

    return target in possible




partitionEqualSum([1,5,11,5])