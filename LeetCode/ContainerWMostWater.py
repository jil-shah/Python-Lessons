# Problem 5 --- Container With Most Water

# **LeetCode 11 --- Medium**

# You are given heights such as:

# ``` text
# [1, 8, 6, 2, 5, 4, 8, 3, 7]
# ```

# Choose two lines that hold the most water.

# figure out the match, most water is the volumn w*h
# w = right - left ; h = min of the two walls 
# want to store the one with max 
# python try (right -left) * (min(l or r wall)) 

# brute force: try every combination. 
# 1, 8 -> 1,6 -> 1,2 -> 1,5 
# O(n^2) -> because we need to go through the whole set 

# width = 8-0 = 8, height = min(1,7) the shorter one limits us so 8 * 1 = 8
# width = 8
    # 8
    # 3; limited by 3 = 5*15
# the height is always the issue when getting smaller 
# so what we can do is place a pointer on both ends 
# l = 1, r = 7: min is 1  so move shorter wall 
# 8, 7 : min 7 shift in 
# 8, 3

def MaxContainerVol(hs):
    l = 0 
    r = len(hs)-1
    maxV = 0
    while ( l < r):
        # can we assume hs is a unique list of numbers?or this may not matter because the number is the same 
        if (hs[l] < hs[r]):
            l +=1
        else:
            r -=1
        tempVol = (r-l) * (min(hs[l],hs[r]))
        maxV = max(maxV, tempVol)
    return maxV

hs = [1, 8, 6, 2, 5, 4, 8, 3, 7]    
print(MaxContainerVol(hs))



