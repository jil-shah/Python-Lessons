# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# 1. anagram is when the same characters are in 2 words
# 2. counts of characters are the same 
# 3. order the words in alphabetical order and then see if the words are the same
# 4. O(nlogn) - n to compare the string, and logn is ordering the string
# 5. ordering is hard
# 6. use a dictionary which resolves the need for ordering 
# 7. maitain the count of each letter
# 8. {a:3, n:1, g:1, r:1, m:1} 
    # n: {a:3, n:0, g:1, r:1, m:1} a: {a:2, n:0, g:1, r:1, m:1}
    # g: {g:0}, a {a:1}, r: {r=0} , a: {a:0} m:{m:0} {a:1, n:0, g:0, r:0, m:0}
    #return true



def validAnagram(word1, word2):
    count1 = {}
    for char in word1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    for char in word2:
        if char in count1 and count1[char] > 0:
            count1[char]-=1
        else:
            return False
    return True
             
# Example 1:
# Input: 
s = "anagram"
t = "nagaram"
# Output: true
print(validAnagram(s,t))
# Example 2:
# Input: 
s = "rat"
t = "car"
# Output: false
print(validAnagram(s,t))
    