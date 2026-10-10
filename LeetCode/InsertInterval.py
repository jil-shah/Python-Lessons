# Problem 2 — Insert Interval (LC 57)
# Input:

# intervals = [[1,3], [6,9]]
# newInterval = [2,5]

# Output:

# [[1,5], [6,9]]

# Problem: we have intervals which are ordered
# we want to insert a new interval within the range

# 1,3 -> 6,9 
# insert -> 2,5. 2 <= 3. which means it fits in the range
# max(3,5) = 5 update node 
# [1,5], [6,9]

# Brute Force: 
# 3 possibilities
# interval is completely before the new one -> insert.end < interval.beg
# overlapps -> it overlaps which means like 1,4 and 2,3 and then update
# after -> append it 

# already sorted and disjoint 
# we start at the index 0
# check if the new.end < interval.beg -> append it before starting  
# check if it fits: interval.end <= new.beg; update the range and append
# check if it is after interval.end < new.beg, append it and then the continue

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

def insertinterval(intervals, insert):
    results = []
    i = 0

    # before skip
    while (i < len(intervals) and intervals[i][1] < newInterval[0]):
        results.append(intervals[i])
        i +=1
    #overlap - merge
    while(i < len(intervals) and intervals[i][0] <= newInterval[1]):
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i+=1
    results.append(newInterval)
    #after - skip
    while(i < len(intervals)):
        results.append(intervals[i])
        i+=1
    return results
    
print(insertinterval(intervals, newInterval))

# Time: O(n)

