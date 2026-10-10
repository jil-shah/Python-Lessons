# LeetCode 49 --- Medium

# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Group words that are anagrams.

# You need:
# representation of an anagram → matching words

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Brute force: compare each letter from each word to the rest of the words- many nested loops
# we have to iterate through all cause we need to return a list
# O(n^2) 

# Idea 2:  order each word in alphabetical order as long as there is no special chacters and can assume all letters are not capitalized
# once ordered compare each word with the rest of the words 
# O(nlogn), nlogn for the ordering and then n for iterating through it 

# Idea 3: order each word in alphabetical order 
# each word check if its in the dictionary, and store it as a dictionary alphabetical -> orginal list 

def GroupAnagrams(words):
    groups={}

    for word in words:
        ordered = "".join(sorted(word))
        if ordered not in groups:
            groups[ordered] = []
        groups[ordered].append(word)
    
    return list(groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagrams(strs))
strs = [""]
print(GroupAnagrams(strs))
# O(k nlogn)