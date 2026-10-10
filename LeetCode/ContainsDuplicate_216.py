# LeetCode 217 --- Easy

# Given an integer array, determine whether any value appears at least twice.

# Input: [1, 2, 3, 1]
# Output: true
# Before coding: - What is brute force? - What is its complexity? - Do you need frequencies, or only whether a value appeared? - What structure answers "have I seen this before?" efficiently?

# Brute force - 2 pointer strategy, start at index 0, and then check if each number to the right is equal, if so true, exit
# keep moving the original index right and then check the remaining values to the right 
# this would be O(N^2) - where N is the length of the array

# Use Set to determine if a value already exists

def AppearsTwice(input):
    Seen = set()
    for i in input:
        if i in Seen:
            return True
        else:
            Seen.add(i)
    return False

numList = [1,2,3,1]
print(AppearsTwice(numList))

# O(n) - only once going through the list once, and space complexity is the same
