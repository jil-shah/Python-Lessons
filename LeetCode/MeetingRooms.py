# Problem 4 — Meeting Rooms (LC 252)
# Can one person attend every meeting?

# [[0,30], [5,10], [15,20]]

# Answer: False.

# Given an array of meeting time interval objects consisting of start and end times 
# [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
# determine if a person could add all meetings to their schedule without any conflicts. 
# The intervals may be provided in any order.

# Note: (0,8),(8,10) is not considered a conflict at 8

# Example 1:
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false

# Problem: 
# there is a list of meeting invites in minutes, and i want to know if i can add all to my calendar
# any order invites

# any overlapping time? false
# none = true 

# 0,30 and 5,10
# overlaps which means 0 < 5 30 > 10
# false
# intervals = [(5,8),(9,15)]
    # 9 >= 8; it will be fine current.start > prevend

# we can compare every time to next
# simplify this by ordering
# lets order by start time 
# and then each index we would compare if the current start is before the previous end
# if it is then we know it overlaps 
# if not no overlap and we move to the next

def meetingrooms(intervals):
    intervals.sort(key=lambda interval:interval[0])
    prevEnd = float('-inf')
    for start,end in intervals:
        if (start < prevEnd):
            return False
        else:
            prevEnd=end
    return True
intervals = [(0,30),(5,10),(15,20)]
print(meetingrooms(intervals))

#O(n log n)
