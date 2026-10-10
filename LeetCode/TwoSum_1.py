# Problem 2 --- Two Sum
# LeetCode 1 --- Easy

# nums = [2, 7, 11, 15]
# target = 9

# Output: [0, 1]
# Brute force tries every pair.

# Ask:

# If I'm currently looking at 7, what value would I need to make 9?

# needed = target - current

# assuming list is ordered, and non negatives 

# brute force start at index 0, and iterate through each value on the right if exists, output the index in an array.
# move the index 0 to the right after every cycle
# O(n^2) where n is the list of numbers

# find the complement of each one (target - current) and store it in a hashset so before we get the complement check if the current value exists in the set
# if it exists return the index of the one in the hashset and the one of the current

def TwoSumFinder(numbers, target):
    complements = {}
    for i in range (0,len(numbers)):
        num = numbers[i]
        if num in complements:
            return [complements[num],i]
        # find the complement
        complement = target - num
        complements[complement] = i
    
nums = [2, 7, 11, 15]
target = 22
print(TwoSumFinder(nums,target))

