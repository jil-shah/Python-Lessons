# 474. Ones and Zeroes

# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's 
# and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.


# Example 1:

# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, 
# so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
# Example 2:

# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.

# Problem: 
# we want to know the combination where the strs that have at most m zeros, and n ones
# running remainder after adding each str

# option: include or not include

# brute force:
# 5 zeros 3 ones
# 10 -> [1,1] -> [4,2]
# 0001 -> [3,1] -> [1,1]
# 111001 -> [2,4] does not satisfy
# 1 -> [1,0]
# 0 -> [0,0]

#     []
# 10[4,2]    0001
#0001[1,1]   111001

# this can eventually repeat for every future subtree
# sub problem: whats the maximum number of string using m and n 
# dp[m][n] means the maximum number of strings you can build for using m zeros and n ones

# if i take zeros,ones -  i now have z-zeros and o-ones left
# state = dp[zeros][ones]
#    0  1  2  3 
# 0  0  0  0  0
# 1  0  0  0  0
# 2  0  0  0  0
# 3  0  0  0  0
# 4  0  0  0  0
# 5  0  0  0  0

#    0  1  2  3 
# 0  0  0  0  0
# 1  0  1  1  1
# 2  0  1  1  1
# 3  0  1  1  1
# 4  0  1  1  1
# 5  0  1  1  1

# 3z, 1o -> take it means 5-3,3-1 = 2,2 -> 1 so 1+1=2
# dont take it = 1 -> dp[5][3] = 2
# 1 one -> take it means 5-0, 3-1= 5,2 -> 1 
# dont take it = 2 means 1+(2,2) = 3
def oneszerosmax(strs,m,n):
    dp = [[0] * (n+1) for _ in range(m)] 

    for str in strs:
        zeros = str.count("0")
        ones = str.count("1")
        for z in range(m, zeros-1,-1):
            for o in range(n,ones-1,-1):
                # number of zeros and ones are my constraint
                dp[z][o] = max(dp[z][o], 1+dp[z-zeros][o-ones])





