# Problem 1 --- Binary Search
# LeetCode 704 --- Easy

# nums = [-1, 0, 3, 5, 9, 12]
# target = 9

# Output: 4
# Before Coding
# Answer:

# What property of the input makes binary search possible? Ordered list can eliminate half the results
# What does left represent? that the target is smaller than nums[mid]
# What does right represent? that the target is larger than nums[mid]
# If nums[mid] < target, which half can be eliminated? The left side is eliminated. 
# Why?

# Time: O(log n)
# Space: O(1)

def BS(nums, target):
    l = 0
    r = len(nums)

    while (l <= r):
        mid = (r+l)//2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            l = mid + 1
        else:
            r = mid - 1
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(BS(nums, target))
            
