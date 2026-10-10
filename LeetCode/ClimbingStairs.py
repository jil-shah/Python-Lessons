# Problem 1 — Climbing Stairs
# LeetCode 70 — Easy
# Full Problem Question
# You are climbing a staircase. It takes n steps to reach the top.
# Each time, you can climb either:
# 1 step
# or
# 2 steps

# In how many distinct ways can you climb to the top?

# Example 1
# Input: n = 2
# Output: 2

# Problem:
# at each step you have an option of taking 1 step or 2 steps
# if we start at 0, we have n steps to climb

# one example: 
# n =2 
# 0,1,2= 2
# 0,2 = 2
# 2 combinations

# lets think about the final 2 moves i can make
# 5 -> 3, 4 and take 2 steps or 1 step
# ways to reach 5 is ways to reach 4 + reach 2
# generalize : ways(n) = ways(n-1) + ways(n-2)
# with this we might see repeatitions ie 
# 5 
    #4
        #3
        #2
    #3
# 3 will get tested 2 
# and eventually lead to slowness

# the states repeat so this is where dp array or table will help

# state: number of ways to reach a particular stair
# final move comes from i-1, or i-2
# so recurrance is finding i-1 or i-2 number of ways
# naive recussion would repeat states
# so computing bottom up may make snese

def climbstairs(n):
    # if (n <=2):
    #     return n

    # dp = [0] * (n+1)

    # dp[1] = 1
    # dp[2] = 2

    # for i in range(3,n+1):
    #     dp[i] = dp[i-1]+dp[i-2]

    # return (dp[n])
    #the above may have repeats
    # what if we always just look at the last 2

    if (n <= 2):
        return n

    onebefore = 2
    twobefore = 1

    for i in range(3,n+1):
        current = onebefore+twobefore

        twobefore = onebefore
        onebefore = current
    return onebefore

# Time: O(n)
# Space: O(1)
print(climbstairs(3))