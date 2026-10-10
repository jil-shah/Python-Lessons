# Problem 3 — Non-overlapping Intervals (LC 435)
# Return the minimum number of intervals to remove so the rest don't overlap.

# [[1,2], [2,3], [3,4], [1,3]]

# Answer: 1.

# Given an array of intervals intervals where intervals[i] = [starti, endi], 

# Note that intervals which only touch at a point are non-overlapping. 
# For example, [1, 2] and [2, 3] are non-overlapping.

 
# Problem
# minimum removals = keep the maximum of non overlapping intervals 
# when 2 intervals compete, we want to keep the one with the earliest ending
# since it ends much earlier and leaves room for other intervals 
# this means we would need to sort by end - since earlier end should always be kept
# then repeatedly compare and keep an interval if 
    # current.start >= previous.end

def erasenonoverlapping(intervals):
    intervals.sort(key=lambda interval:interval[1])
    removals = 0
    prevEnd = float("-inf")

    for start,end in intervals:
        if (start >= prevEnd):
            prevEnd = end
        else:
            removals+=1
    return removals
# O(nlogn)
print(erasenonoverlapping([[1,2], [2,3], [3,4], [1,3]]))





    
