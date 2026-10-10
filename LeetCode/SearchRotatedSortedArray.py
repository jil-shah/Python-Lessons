# Problem 2 --- Search in Rotated Sorted Array
# LeetCode 33 --- Medium

# Example:
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0

# Output:
# 4

# first thing i noticed is this is not sorted easily
# but if you look at the middle the right and left is sorted
# this will help with keeping it O(logn) 
# so nums[mid] = 7; left = 4, right = 2 target = 0 
# nums[left] <= nums[mid] -> 4 <= 7; If true, the left half is sorted.
# else Otherwise, the right half is sorted.
# then search if the target is within the sorted halfs range
# if not search the other half 


def RotatedSorted(nums, target):
    l = 0
    r = len(nums) - 1

    while(l <= r):
        mid = (l+r)//2

        if (nums[mid] == target):
            return mid
        
        if(nums[l] <= nums[mid]):
            if (nums[l] <= target < nums[mid]):
                r = mid - 1
            else:
                l = mid + 1
        else:
            if(nums[mid] < target <= nums[r]):
                l = mid + 1
            else: 
                r = mid - 1
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(RotatedSorted(nums,target))