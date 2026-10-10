# Problem 5 — Task Scheduler
# LeetCode 621 — Medium

# Example:
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
# Each CPU interval can be idle or allow the completion of one task. 
# Tasks can be completed in any order, but there's a constraint: 
# there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

 
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two intervals before doing A again. 
# The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. 
# By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# start with scheduling the one with the largest frequency
# available tasks belong in a max heap
# after scheduling, it cant go back into available heap, it needs to cool down
# cooldown queue: each cooling tasks requires remaining frequency and when its available again (freq, avail)

# choose repeatedly best available task 
# most frequent remaining task is hardest to place
# max heap of available task
# use one task 
# task enters cooldown
# remembers ready time 
# continue until until heap and cooldown are empty

import heapq
from collections import deque

def leastInterval(tasks, n):
    freq = {}
    for task in tasks:
        if task in freq:
            freq[task] += 1
        else:
            freq[task] = 1
    #convert the freq list into a heap 
    heap = [-count for count in freq.values()]
    heapq.heapify(heap)
    # create a cooldown queue that holds the current freq and interval
    cooldown = deque()
    # time incr at every interval
    time = 0 
    # heap is not empty or cooldown is not empty
    while(heap or cooldown):
        time +=1

        if heap:
            #take element from the heap (max pop) so that we get the one that is most freq
            count = heapq.heappop(heap)
            count+=1 #since count is negative
            # add the updated count, and then the new time only if remaining tasks
            if (count != 0):
                cooldown.append((count,time+n))

        # check if the cool down period is done 
        if cooldown and cooldown[0][1] == time:
            count, _ = cooldown.popleft()
            heapq.heappush(heap,count)

    return time

tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks,n))
