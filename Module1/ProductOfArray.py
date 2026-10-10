# 318. Maximum Product of Word Lengths

# Given a string array words, return the maximum value of 
# length(word[i]) * length(word[j]) where the two words do not share common letters. 
# If no such two words exist, return 0.

# Example 1:

# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn". 

# create a set for each work 
# compare each set with the next (O(n^2))
