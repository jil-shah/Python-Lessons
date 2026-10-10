# 4. Problem 3 — Combination Sum (LC 39)

# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less 
# than 150 combinations for the given input.

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# set is unliminited
# start at the highest number 7 
# then it meets target alread we have 1
# 6 - 6+7 nope
#   - 6+6 nope
#   - 6+2 nope 
# 3 - 3+7, 3+6, 3+3 =6 +
# backtrack for each new value and go from largest to smallest

#what decision am i making? building a combination
#i can repeatedly choose so staart a 2,, choose 2 again, then choose 3
# this is like the decision tree
# what state should i track? current, how close am i to the target by summing 
# or instead use remaining
# 7-2 = 5 
# 5 -2 = 3 
# 3-2 = 1
# back track 
# 3-3 = 0; that is a set
# invalid branch, exceeding the target or reaching 1 but no 1 in the nums
# problem is duplicates how do we prevent them 
# how can we prevent from going backgrounds
# once i move forward, dont go backward
# 0: 2, 3,6,7
# recurssion, since we can rechoose the same number, we dont move to next index
# chose 
# append candidate
# explore
# remaining -candidate
# unchoose
# pop

def combsum(nums, target):
    results = []
    current = []

    def backtrack(i, remain):
        if (remain == 0):
            results.append(current.copy())
            return
        elif(remain < 0):
            return
        for i in range(i,len(nums)):
            current.append(nums[i])
            backtrack(i,remain-nums[i])
            current.pop()


    backtrack(0, target)
    return results

candidates = [2,3,6,7]
target = 7
print(combsum(candidates, target))