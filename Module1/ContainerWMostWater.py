# 11. Container With Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are 
# (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.

# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
                #  0 1 2 3 4 5 6 7 8 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Input: height = [1,1]
# Output: 1

# start with the widest and go smaller but keep the max height 
# l = 0 r = 8 minh = 1; 1 * 7 = 7. Keep r
# l = 1 r = 8 minh = 7; 7 * 7 = 49. keep l
# l = 1 r = 7 minh = 3; 3 * 6 = 18. keep l
# l = 1 r = 6 minh = 8; 8 * 5 = 40

def maxVol (lines):
    l = 0 
    r = len(lines)-1
    maxV = 0
    while(l < r):
        minh = min(lines[l],lines[r])
        maxV= max(maxV, minh * (r-l))
        if (lines[l] <= lines[r]):
            l+=1
        else:
            r-=1
    return maxV

height = [1,8,6,2,5,4,8,3,7]
print(maxVol(height))