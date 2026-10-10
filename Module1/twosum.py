# 1. Two Sum

# You are given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# 1. problem is asking to find 2 numbers that add to the target. return only index
# 2. sum of a + b = target 
# 3. add every index of numbers using two pointer 
    # Input: nums = [2,11,7,15], target = 9
    # 2 + 11 = 13 [0,1]
    # 2 + 7 = 11 [0,2]
# 4. Brute force would be every index evaluated
# 5. searching is expensive
# 6. if we instead use a heap, we care about 2 values number and the index.
# Input: nums = [2,11,7,15], target = 9
    # heap:{} 9-2 = 7, 7 not in heap, add the value {2:0}
    # {2:0}, 9-11 < 0 11 is out of scope 
    # {2:0}, 9-7 =2, 2 in heap return current index and value of the key [2,0]

# 7. i am maintaining the index and the value
# 8. dry run above
# 9.  heap is O(1) and go through once so o(n)
# 10. approach would be for each i in nums, see if the remainder exists in the database
# if it does then return the two integers value and the current index
# if its less than 0 skip, number is too big
# if doesnt exist in the heap, then add the current value and index

def twosum(nums,target):
    seen = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if (diff not in seen):
            seen[nums[i]] = i
        else:
            return([i,seen[diff]])
nums = [2,11,7,15]
target = 9
print(twosum(nums,target))
nums = [3,2,4]
target = 6
print(twosum(nums,target))

def twosum2(nums,target):
    seen = {}

    for i, num in enumerate(nums):
        compl = target - num
        if (compl in seen):
            return [i,seen[compl]]
        else:
            seen[num] = i
nums = [2,11,7,15]
target = 9
print(twosum2(nums,target))
nums = [3,2,4]
target = 6
print(twosum2(nums,target))