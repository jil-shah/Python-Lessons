# 3. Problem 2 — Permutations (LC 46)
# Subsets ask “take or skip?”
# Permutations ask:

# Which UNUSED number goes in this position?
# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.
# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# it has to have all three numbers 
# so instead of asking take or skip, its is the number index already in this position
# base case would len(current) == len(nums)

# for each unused number, append it, mark as used, recurse, pop it, and unmark used

def permutation(nums):
    results = []
    current = []
    used = set()

    def backtrack():
        if (len(current) == len(nums)):
            results.append(current.copy()) # current is constantly changing
            return
        
        for num in nums:
            if (num in used):
                continue
            current.append(num)
            used.add(num)

            backtrack()

            current.pop()
            used.remove(num)

    backtrack()
    return(results)

nums = [1,2,3]
res = permutation(nums)
print(res)