# 49. Group Anagrams
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# PROBLEM:
# we have a list of words, and want to know if they can be anagrams of eachother
# we know if its an anagram if the same letters appear in both words

# so one way i can think of to see if a word belongs in an anagram is by ordering the string in alphabetical order and then comparing it 
# this mean we would scan each word, rearrange the letters and then save it 
# once we converted we can compare with eachother 

# another way is utilize a dictionary 
# so eat -> aet and then in the dictionary we store aet -> ["eat"] 
# then preform tea -> aet, we store it aet ->["eat", "tea"]

# O(nlogn  for the sort, and then adding and comparing with dictionary is 1)

def groupanagrams(words):
    ordered = {}
    for word in words:
        # is this case sensitive? 
        sort = "".join(sorted(word))
        if sort in ordered:
            ordered[sort].append(word)
        else:
            ordered[sort] = [word]

    return (list(ordered.values()))

print(groupanagrams(["eat","tea","tan","ate","nat","bat"]))