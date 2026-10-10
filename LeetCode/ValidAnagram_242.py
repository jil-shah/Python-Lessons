# Problem 3 --- Valid Anagram
# LeetCode 242 --- Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# brute force: take each character in the first word and search for it in the second, and record indexes that have already been found
# O(n^2) since each word needs to be iterated and 
# Order by alphabets and then compare the string 
# O(nlogn) - sorting is the consuming step

# dictionary of one and then go through each letter of t and see if the letter exists if it does subtract 1 from the dictionary 

def ValidAnagram(s, t):
    #if words length are different not valid anagram
    if len(s) != len(t):
        return False
    # build the dictionary of the first word
    sdic = {}
    for char in s:
        if char in sdic:
            sdic[char]+=1
        sdic[char] = 1
     
    # compare each letter of word t
    for char in t:
        if char in sdic:
            sdic[char]-=1
        else:
            return False
    return True
# O(n + m) = O(n) creates map of the first one and then iterate through the second one
s = "anagram"
t = "nagaram"
        
print(ValidAnagram(s,t))

s = "rat"
t = "car"
print(ValidAnagram(s,t))