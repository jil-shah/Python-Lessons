# 167. Two Sum II - Input Array Is Sorted

# You are given a 1-indexed array of integers numbers that is already sorted in 
# non-decreasing order.

# Find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2 as an integer array 
# [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. 
# You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# we can add each possibility to add to 9 
# the problem here will be trying each combination is not worth it since the list is ordered
# 0(n^2)
# we can do this by visiting each number once
# start at l= 2, r = 15 target = 17. 17> 9, number needs to be smaller shift r
# l =2 r = 11. t = 13. 13>9. shift r
# l=2 r = 7. t = 9. 9=9. done 

def twosum (nums,target):
    l = 0
    r = len(nums)-1
    while(l < r):
        sum = nums[l]+nums[r]
        if (sum > target):
            r-=1
        elif (sum < target):
            l+=1
        else:
            return[l+1,r+1]
    return []

numbers = [2,7,11,15]
target = 9
print(twosum(numbers,target))