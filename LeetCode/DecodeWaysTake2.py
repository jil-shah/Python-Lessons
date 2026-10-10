
# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# Problem: is we want to know how many possibilities there are to decode a message
# 1. a valid character is between 1-26
# 2. one digit - 1-9 
# 3. two digits - 10-26

# Choices: 
# take one or take 2 

# Brute Force
# 11106
#      []
#   1     11
# 1  11 1    10
# 
# Smaller Problem 
# does the numbers we choose exist in the range
# dp[i] how many ways can i decode the first characters
# 1 - [1]
# 1,11 - [1,2]

# dp[0] = 1
# and then each index = dp[1] = 1 + dp[0]
# dp[2] = 1+ dp[1]

def decode(word):
    dp = [0] *(len(word)+1)

    dp[0] = 1

    for i in range (1, len(word)+1):
        if(dp[i-1] != "0"):
            dp[i] += dp[i-1]

        if( i >= 2 
            and 10 <= int(dp[i-2:i]) <=26
           ):
            dp[i] += dp[i-2]

    return dp[len(word)]
        
