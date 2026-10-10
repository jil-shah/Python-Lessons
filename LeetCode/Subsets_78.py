# 2. Problem 1 — Subsets (LC 78)
# For every number, choose TAKE or SKIP.

# For [1,2]:
# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Know
# any range subset? yes 
# any combination must not repeat
# output is a list of lists
# every number has a choice, either we take/skip 

# this can be viewed as a decision tree 
# go through each combination of the decision tree
# use a dfs and then export the output by going through each possibility 

def subsets(nums):
    current = []
    results = []

    def backtrack(index):
        # base case when len of nums is reached
        if (index == len(nums)):
            results.append(current.copy())
            return
        current.append(nums[index])
        backtrack(index+1)
        current.pop()
        backtrack(index+1)

    backtrack(0)
    return (results)

# Time: O(n·2^n) including output copying.

nums = [1,2,3]
print(subsets(nums))