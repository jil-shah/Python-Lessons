# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# 1. the problem is to idenitfy if there is any repeated numbers
# 2. find the first repeated number and return true 
# 3. brute force check every value and then the rest of the numbers to see if it repeats
# 4. n^2 each number we would iterate through the rest of the numbers 
# 5. the repeated iterations 
# 6. use a hash set. if any number is found in set return true
# 7. maintaining the hash set
# 8.
    # 1: nothing in set add 1 {1}
    # 2: {1} 2 not in set add 2
    # 3: {1,2} 3 not in set add 3
    # 1: {1,2,3} 1 in set return true 
# 9. O(N)

def containsdupe2(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

def containsdupe(nums):
    seen = set(nums)
    if (len(seen) == len(nums)):
        return False
    return True

# Example 1:
nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
print(containsdupe(nums))
# Example 2:
nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.
print(containsdupe(nums))
# Example 3:
nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
print(containsdupe(nums))