# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
# or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# letters dict count 
#s1: a = 1, b = 1 ... z
#"ei": s2: e = 1, i = 1

# we can just iterate through it but now the issue becomes (O(26*N))
# Instead if we keep track of the matches from the beginning 
# matches = a,b and all 0 = 26 -4 = 22
# iterate through s2 using the size of s1 
# ab = 2; l = 0, r =1
# matches != 26 we need to align 
# r=2; d; e = 1, i = 1, d = 1; matches = 21 
# l=0;  ; e = 0, i = 1, d = 1; matches = 22
# r=3; b; b = 1, i = 1, d = 1; matches = 23
# l=1;  ; b = 1, i = 1, d = 0; matches = 24
# r=4; a; a = 1, b = 1, i = 1; matches =25
# l=2;    a = 1, b = 1, i = 0; matches=26
import string

def perminstring(s1,s2):
    if (s1 > s2):
        return False
    # empty dict
    s1dict = {char: 0 for char in string.ascii_lowercase}
    s2dict = {char: 0 for char in string.ascii_lowercase}

    for i in range (len(s1)):
        s1dict[s1[i]] += 1
        s2dict[s2[i]] += 1

    #count matches
    matches=0
    for char in string.ascii_lowercase:
        matches += (1 if s1dict[char] == s2dict[char] else 0)

    # iterate through list
    l = 0
    for r in range (len(s1), len(s2)):
        if (matches == 26):
            return True

        rc = s2[r]
        s2dict[rc] += 1
        if (s1dict[rc] == s2dict[rc]):
            matches+=1
        # if by adding the character we lost a match
        elif (s1dict[rc]+1 == s2dict[rc]):
            matches -=1

        lc = s2[l]
        s2dict[lc] -= 1
        if (s1dict[lc] == s2dict[lc]):
            matches+=1
        # if by removing the character we lost a match
        elif (s1dict[lc]-1 == s2dict[lc]):
            matches -=1
        l+=1
    return matches == 26


# Example 1:
# Input: 
s1 = "ab"
s2 = "eidbaooo"
print(perminstring(s1,s2))
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
