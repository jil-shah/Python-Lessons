# Problem 5 --- Merge Two Sorted Lists
# LeetCode 21 --- Easy

# 1 → 2 → 4
# 1 → 3 → 4
# becomes:

# 1 → 1 → 2 → 3 → 4 → 4

# have 2 nodes for list 1 and list 2 and a new list 
# compare node 1 from both lists and see which is larger
# 1 >= 1; place node 1 from list 1 and shift the node None -> 1
# 2 >= 1; place node 1 from list 2 and shift the node None -> 1 -> 1
# 2 <= 3; place node 2 from list 1 and shift the node None -> 1 -> 1 -> 2
# 4 <= 3; place node 2 from list 2 and shift the node None -> 1 -> 1 -> 2 -> 3

# this means we need to loop as long as a next value exists 
# rather than a new list what if its just adding to the first list 

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val=val
        self.next=next

def mergeSortedList(head1, head2):
    dummy = ListNode()
    tail = dummy
    while(head1 and head2):
        if (head1.val < head2.val):
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next     

    tail.next = head1 if head1 else head2

    return dummy.next