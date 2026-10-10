# Problem 4 --- Longest Substring Without Repeating Characters
# LeetCode 3 --- Medium

# Find the length of the longest substring containing no repeated characters.
# Example:
# s = "abcabcbb"
# Answer: 3

# Brute Force: check every letter in the string and use some kind of set for unique characters
# a # starting letter index, add to set
# a -> b # shift index 2 to go through the rest of the list, loop through the current string set to see if a character is repeated, if not add to arr
# a -> b -> c # shift, add to set
# a -> b -> c -> a # a is in the set, exit inner loop, max = 3, reset the set 
# b 
# b -> c -> a -> b # b is in the set, exit inner loop, max = 3

# O(n^3): because every letter we would have to compare against the word set
# O(size of list)

# better idea: 
# use a left right pointer and a set 
# a -> l/r ; expand l=0, r = 0
# a b ; b is unique; expand l=0, r=1
# a b c ; c is unique; expand l=0, r=2
# a b c a ; a is not unique; shift left, max is 3 l=1, r=3
# b c a b ; b is not unique shift left, max is 3 l=2, r=4
# c a b c ; c is not unique shift left, max is 3 l=2, r=5

def LongestSubstring(input):
    lett = set()
    l = 0
    tempmax = 0
    for r in range (len(input)):
        
        # lett.remove(input[l]) # but what if the repeated letter is not the first letter everytime 
        while(input[r] in lett):
            lett.remove(l)
            l+=1
        lett.add(input[r])
        tempmax = max(tempmax, r-l+1)
    return tempmax

    
s = "abcabcbb"
print(LongestSubstring(s))

