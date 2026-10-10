# Problem 4 — Word Break
# LeetCode 139 — Medium
# Full Problem Question
# Given a string s and a dictionary of strings wordDict, 
# return True if s can be segmented into a sequence of one or more 
# dictionary words.

# You may reuse words from the dictionary.

# Example
# Input:
# s = "leetcode"
# wordDict = ["leet", "code"]

# Output:
# True
# Explanation:
# "leetcode"
# =
# "leet" + "code"

# 1. What is the problem really asking?
    # do the letters in s belong to a words dict
    # can i split the entire string into valid dictionary words
    # answer is either true or false
# 2. What choices exist?
    # where do i split the string
    # possible split options
# 3. Can I write a recursive/brute-force version conceptually?
    # at each range, it exists in word dict
    # dp[i] the word exists
    # for very possible word starting here 
    # if in the dictionary then recursively solve the remainder
# 4. What smaller problem does each choice lead to?
    # smaller problem is s[i:j] exists in the database
    # leet found, then problem is can i break code
    # starting at 0, and then starting at index 4
# 5. Do those smaller problems repeat?
    # yes for each range check if it exists
    # s[:j] exists in the database 
    # we would be checking each possible outcome split at each index 
# 6. What information uniquely identifies one smaller problem?
    # once at a position in the string, where are we, the smaller problem is i/prefix length
# 7. State explicitly: “dp[...] means ______.”
    # dp[i] first i chatacters can be segmented
# 8. What is the recurrence?
    # at each range check. check before i and then everything from[i:j]
# 9. What is the base case?
    # dp[0] = True
    # because we have used 
# 10. In what order must states be calculated?
    # check s[:j] s[j:i]
    # the prefix through j must be segmentable
    # s [j:i] must be dictionary word
    # if dp[j] and s[j:i] in wordset
# 11. Can space be optimized?
# 12. What are time and space complexity?

def wordBreak(s, wordsDict):
    words = set(wordsDict)
    dp = [False] * (len(s) +1)
    dp[0] = True
    for i in range(1,len(s)+1):
        for j in range(i):
            if (s[j:i] in words):
                dp[i] = True
                break
    return dp[len(s)]

s = "leetcode"
wordDict = ["leet", "code"]

print(wordBreak(s,wordDict))
