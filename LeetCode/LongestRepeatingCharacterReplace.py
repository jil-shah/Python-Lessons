# 424. Longest Repeating Character Replacement
# Medium
# Topics
# premium lock icon
# Companies
# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Problem:
# we want find the longest substring with the same letter
# is it only uppercase? yes

# we keep the same letter 
# we change the letter

# will k ever be greater than the length of the string? Nope

# Brute Force 
# find the unique characters {a,b}
# iterate through the list k*len(s) and try all combinations
# this isnt the most efficient 
# multiple iterations of the string 

# another idea is 
# use a sliding window
# we know the max number of changes we can make is k
# we want to replace the character that are less frequent within a window
# valid window would be where window size - max frequency <= k
# if the condition becomes false, we need to reduce the window size
# shift the 0th pointer to the next character, and essentially do this until the right pointer reaches the end 

def replacecharacters(s, k):
    r = 0
    l = 0 
    freq = {}
    maxFreq = 0
    while(r <= len(s)-1):
        if (s[r] in freq):
            freq[s[r]] +=1
        else:
            freq[s[r]] =1
        tempMax = max(freq.values())

        while((r-l+1) - tempMax > k):
            freq[s[l]] -=1
            l+=1
        maxFreq = max(r-l+1, maxFreq)
        r+=1
    return maxFreq
       
# O(N) and O(N)

s = "AABA"
k = 1

print(replacecharacters(s,k))