# Problem 5 — Longest Increasing Subsequence
# LeetCode 300 — Medium
# Full Problem Question
# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence.

# A subsequence is formed by deleting zero or more elements 
# without changing the order of the remaining elements.

# The elements do not need to be adjacent.

# Example
# Input:
# nums = [10,9,2,5,3,7,101,18]

# Output:
# 4

# One longest increasing subsequence is:

# [2,3,7,101]

# Its length is:

# 4

# Problem:
# Find the longest increasing sequence
# Choices:
# Include or Not Include
# 3. Can I write a recursive/brute-force version conceptually?
    # 1 + dp[n-1] 
# 4. What smaller problem does each choice lead to?
    # find any number where nums[current] < nums[prev]. 
    # for each calculate dp[i]
    # take the max of dp[i]  
# 5. Do those smaller problems repeat?
    # yes 
# 6. What information uniquely identifies one smaller problem?
    # count of max elements for the previous numbers
# 7. State explicitly: “dp[...] means ______.”
    # dp[i] -> means the maximum number of elements until nums[i]
# 8. What is the recurrence?
    # number find the max for each i 
# 9. What is the base case?
    # dp[0] = 1
    # for each i minimum is 1
# 10. In what order must states be calculated?
    # from left to right, so that smaller i's are already calculated
    # so at i, you need to look through 0: i
# 11. Can space be optimized?
# 12. What are time and space complexity?
nums = [10,9,2,5,3,7,101,18]

def longestSequence(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if (nums[j] < nums[i]):
                dp[i] = max(
                    dp[i],
                    dp[j] + 1
                )
    return max(dp)

print(longestSequence(nums))



