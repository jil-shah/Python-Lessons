# 377. Combination Sum IV

# Given an array of distinct integers nums and a target integer target, 
# return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0

# Problem: we want to find the number of combination to reach the target
# and we can reuse any of the numbers 

# choices: take or skip 
# Brute force: 
# 1,2,3 target 4
#        []
#      1     R = 3
# 1[2]  2[1]  3[0]  ; we found one combination 
# 1[1]
# 1[0]               ; we found a combination 

# this means that we need to get to 0 and need to know the how many ways to get there
# since we know there can be repeated combinations

# smaller problem: how many combinations do we have to reach each target
# dp[i] this would be the number of combinations to reach i 
# dp[0] - use 0 integers. This means we have 1 way to reach 0
# dp[1] - try each number, if it works add 1 
    # dp[1]+= 1
# dp[2] - try each number, if it works add 1 = 2
    # 1: 2 is the target, coin is 1. 2 -1 >=0, then dp[2] += dp[2-1=0]
    # 2: 2 is the target, coin is 2. 2>= 2 then dp[2]+= dp[0] 
# dp[3] 
    # 1: 3 is ther target, coin is 1. 3-1 = 2>= 0, then dp[3] += dp[3-1=2] = 2
    # 2

# O(N*k) so we would need to iterate through 0-target 
# and then go through each num in nums 

def combinationsum(nums,target):
    dp = [0] * (target + 1)

    dp[0] = 1
    for curr_target in range (1, target+1):
        for num in nums:
            if (curr_target - num >= 0):
                dp[curr_target] += dp[curr_target-num]
    return dp[target]