# Problem 3 --- Two Sum II
# LeetCode 167 --- Medium

# You are given a sorted array and a target.
# Find two numbers whose sum equals the target.

# Example:
# numbers = [2, 7, 11, 15]
# target = 9

# Assume: that the number are in inc order, and 
# Brute Force: compare each number with the next and check if the sum is equal to the target. 
# 2+7, 2+11, 2+15
# this would mean that time complexity O(n^2) and space complexity is 0(1)

# use the left and right pointer
# move the pointer based on if the number is bigger and larger than target
# 9 < 17, L pointer to the right. 
# return True if its the same

# O(N) for time, and O(1)
def TwoPointer(nums, target):
    l = 0
    r = len(nums)-1

    while (l < r):
        tempsum = nums[l]+nums[r]
        if (tempsum < target):
            l+=1
        elif (tempsum > target):
            r-=1
        else: 
            return [nums[l],nums[r]]


numbers = [2, 7, 11, 15]
target = 9 
print(TwoPointer(numbers, target))