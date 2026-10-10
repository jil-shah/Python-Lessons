# 91. Decode Ways

# Problem:
# I want to know the number of variations that a message can be decoded too

# Example
# 1 = A or 11 = K
# 11106
# Each s[i:j]
# we have two options take the letter i
# or we take i:i+1

# Edge case: 
# does "0" mean return 0? 

# We know that a valid range of numbers is 1-26. 
# we dont really care about the output string, just if the numbers are in the range
# we dont need a dictionary we can just check if the number is valid 

# how would iterating work 
# []
#     1            11
#  1     11      1    10
# 1 10  0  06   0 6  6

# we can see that it forms a tree of choices 
# we also can see the end results ask similar questions: does the value exist in the range 
# dp[i] is how many ways can i decode the first i characters 
# dp[0] - 1
# i = 1 ; dp[1] = 1 + dp[0]
# dp[2] = current is valid = 1, current i and i-1 = valid = 1+1 =2
# notice we only care about i-1, or i-2, we can simplify

# how do we know if the string has fully been evaluated
# we reach end of the string, and if we do, we add one to the counter

def decodeways(s):
    dp = [0] * (len(s)+1)
    dp[0] = 1
    for i in range(1,len(s)+1):
        # one digit
        if (s[i-1] != "0"):
            dp[i] += dp[i-1]
        #take two digits
        if (i >=2 and s[i-2] != "0" and 10 <= int(s[i-2 : i]) <= 26):
            dp[i] += dp[i-2]
    return dp[len(s)]


print(decodeways("12"))

    