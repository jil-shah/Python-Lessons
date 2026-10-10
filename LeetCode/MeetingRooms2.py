# Problem 5 — Meeting Rooms II (LC 253)
# Return the minimum number of rooms required.

# Given an array of meeting time interval objects consisting of start and end times
#  [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
# find the minimum number of rooms required to schedule all meetings without any conflicts.

# Note: (0,8),(8,10) is NOT considered a conflict at 8.

# Problem: you have meetings but need to know how many roomw you need
# overlapping meetings requires the maximum number of overlapped meetings
# consecutive non overlapping meetings can be done in the same room, dont increment 
# assuming that the list is not ordered

# since to see overlapping meeting we would need the list to be ordered 
# order by start time 

# we always want to compare against the larger range 
# 0,30 and 5,10  5>30 which means it overlaps; +1;
# then move to the next index 15,20 15> 10 so the same room as 5,10 can be used

# indicates that we need to know current, and then prev min ending 
# this means that we always want the prev min so we can use a min heap 
# we only need prev end times

# we start with 0,40 
# there is nothing in the heap. min heap = 40. add 1 to room
# (5,10) -> minheap = 40. 5 < 40; overlapped meeting 
# (15,20) -> minheap = 10. 15 > 10 last meeting was already done. 15 <= 30; overlapping 1 meeting
import heapq
def meetingrooms(intervals):
    intervals.sort(key=lambda interval: interval[0])
    heap = []
    maxm = 0

    for start, end in intervals:
        while(heap and start>=heap[0]):
            heapq.heappop(heap)
        
        heapq.heappush(heap, end)
        maxm = max(maxm, len(heap))
    return maxm

print(meetingrooms([[1,4], [2,5], [6,8]]))
# 2