# Problem 1 --- Valid Palindrome
# LeetCode 125 --- Easy
# Determine whether a string is a palindrome after ignoring non-alphanumeric characters and capitalization.
# Example:
# "A man, a plan, a canal: Panama"
# → "amanaplanacanalpanama"
# Output: True

# simple: 
# 2 Pointer: left pointer checks if its equal to right pointer
# added complexity: only if they are both non-alphanumeric, if not convert to the same case and then compare
# O(n)
def ValidPalindrome(words):
    l = 0
    r = len(words)-1
    while (l < r):
        while (l < r and words[l].isalnum() == False):
            l+=1
        while(l < r and words[r].isalnum() == False):
            r-=1            
        if (words[l].lower() != words[r].lower()):
            return False
        l+=1
        r-=1
            
    return(True)


words = "A man, a plan, a canal: Panama"

print(ValidPalindrome(words))