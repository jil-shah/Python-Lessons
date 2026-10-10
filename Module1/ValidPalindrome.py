# Valid Palindrome
# reads the same left and right

# base idea: go left to right and right to left error if its not
# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include 
# letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# str.isalnum() method returns True if all characters in a string are alphanumeric

def validpalindrome(word):
    # for i in range (0,len(word)):
    #     for j in range(len(word)):
    #this makes it O(N^2)
    l = 0
    r = len(word)-1
    while (l < r):
        #shift left until valid character
        while (l < r and word[l].isalnum() == False):
            l += 1
        while (r > l and word[r].isalnum() == False):
            r-=1
        if (word[l].lower() != word[r].lower()):
            return False
        l += 1
        r -= 1
    return True

print(validpalindrome("A man, a plan, a canal: Panama"))
