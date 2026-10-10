# Problem 6 --- Linked List Cycle
# LeetCode 141 --- Easy

# Normal:

# 1 → 2 → 3 → 4 → None
# Cycle:

# 1 → 2 → 3 → 4
#         ↑     ↓
#         ← ← ←

# Brute Force: use a set(), so we check if every node already exists, if it exists then we know its a cycled list
# however for this we would go through the entire list 0(n) and 0(n) because of the set
# O(1)? For this using slow and fast pointer, eventually slow and fast would equal. If one reaches none it is not cycled



class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def isCycle(head):
    sp = head
    fp = head
    while (fp and fp.next): # we always need fp.next.next
        sp.next
        fp.next.next
        if (sp == fp):
            return True
    
    return False


