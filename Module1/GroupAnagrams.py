# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.


# compare each letter to each string
# reorder the letters and store the reordered as the key, the value is all the words that fit
# aet: eat, tea, ate
# ant: tan, nat
# abt: bat
# and then return the values as nested array
# O(logn) to sort, and then k for the list of the words

def GroupAnagrams(words):
    ordered = {}
    for word in words:
        #order the word
        sortedW = "".join(sorted(word))
        if sortedW in ordered:
            ordered[sortedW].append(word)
        else:
            ordered[sortedW] = [word]

    return list(ordered.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagrams(strs))

#remember 
# order a word alphabetically: "".join(sorted(word))
# return a list from dictionary: list(ordered.values)