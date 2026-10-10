# Problem 1 — Merge Intervals (LC 56)
# Input:

# intervals = [[1,3], [2,6], [8,10], [15,18]]

# Output:

# [[1,6], [8,10], [15,18]]

# Problem: 
# we want to combine overlapping ranges until the output does not have any
# First Test:
# [1,3], [2,6] -> 1,3 2 falls in that range so there is overlapping 

# Brute force: 
# 1. Compare each pair against one another 
#   but what if the list is unordered 
# 2. Can i sort them to ensure its ordered
# 3. What past information do i need?
#   - if its already ordered, then i only need previous one
# 4. derive cases
# [2,6]
# [1,3]
# 2<=3 so they overlap 
# new end max(3,6) = 6
# so (1,6)
# max because we need the highest of the two ranges 
# but what if [1,6], [8,10] -> then 8 not <= 6, which means dont append it 

def Merger(ranges):
    ranges.sort(key=lambda range: range[0])
    merged = []

    for range in ranges:
        if not merged or range[0] > merged[-1][1]:
            merged.append(range)
            continue
        else:
            merged[-1][1] = max(range[1], merged[-1][1])
    return merged

intervals = [[1,3], [2,6], [8,10], [15,18]]
print(Merger(intervals))
# O(nlogn)
# O(n)
