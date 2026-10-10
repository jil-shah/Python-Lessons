# Problem
# find the maximum amount of money after robbing houses 
# 1. two side by side houses cant be robbed

# Choices: Skip/Rob 
# Brute Force:
# [1,2,3,1]
# 1 -> skip or rob
# rob = 1, skip 2, rob 3: total = 4
# rob = 2, skip 3, rob 1: total = 3

# so if rob house i, then we cannot rob house i-1
# if we dont rob house i, then we choose the best one before i 

# smaller problem we are trying to solve is 
# do we get the maximum money if we rob one_previous or two_previous 
# dp[m] -> maximum money that i can rob
# rob house i, then the next best option is i-2
# skip house i, then the next best option is i-1

# because we only care about the previous 2, we dont need to store an array

def robber(houses):
    oneback = 0
    twoback = 0

    for house in houses:
        rob_current = house + twoback
        skip_current = oneback
        maxM = max(rob_current, skip_current)
        twoback =  oneback
        oneback = maxM
    return oneback
robber([2,7,9,3,1])