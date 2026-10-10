# Problem 2 --- Move Zeroes
# LeetCode 283 --- Easy

# Move all zeroes to the end while maintaining the relative order of
# non-zero elements.

# Do it in place.

# Example:
# Input:
# [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]

# Brute Force: add all zeros to a new list. Then fill in the remaining with zeros 
# O(n) for the iteration, and then O(n) for space too because of the additional list
# Solution: fast slow pointer
# we want to move all non zero to the right. so the left pointer will be slower than the right
# so the right pointer goes through each number, if the number is non-zero then switch with left, left increments by 1
# l = 0, r = 0 -> r is zero, so increment r 
# l = 0, r = 1 -> r is non-zero, switch so [1,0,0,3,2], increment l 
# l = 1, r = 2 -> r is zero, increment
# l = 1, r = 3 -> r is non-zero, switch so [1,3,0,0,2], increment l
# l = 2, r = 4 -> r is non-zero, switch so [1,3,2,0,0]
# O(n) and O(1) for space

def MoveZeros(nums):
    l = 0
    for r in range(len(nums)):
        if (nums[r] != 0):
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
    return nums

nums = [0, 1, 0, 3, 12]
print(MoveZeros(nums))

