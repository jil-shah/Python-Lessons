# Problem 
# we want the minimum number of coins to make the target value
# we have choices which is the list of coins
# Brute Force
# 11 [1,2,5]
# 1->10, 2-> 8, 5-> 3, 2 -> 1, 1-> 0
# we need to go through all possibilities 
# smaller problem?
# suppose i choose 5? then 11-5 = 6, then now subproblem i am solving is min num of coins to make 6
# repeat? yes because we can potentially get the same amount and then the number of coins would be the same
# ie 11-2-2-1 = 6 and we went through 11-5 = 6, then we are resolving dp[6] twice

# dp[x] it means the minimum number of coins required to sum x
# base case: dp[0] = 0 coins
# we want to stop when we go through all combinations because we need the minimum 

def mincoins(coins, target):
    dp = [float("-inf")]*(target + 1)
    dp[0] = 0

    for current in range (1, target+1):
        for coin in coins:
            if (current - coin>=0):
                dp[current] = min(dp[current], 1+dp[current-coin])

    return dp

mincoins([1,2,5],11)