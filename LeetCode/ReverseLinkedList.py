# Problem 4 --- Reverse Linked List
# LeetCode 206 --- Easy

# 1 → 2 → 3 → 4 → None
# becomes:

# 4 → 3 → 2 → 1 → None

# will there be any null mid inputs do we care
# Brute force: iterate through the list

# so 1 -> 2 becomes 2 -> 1
# for this to work we need to know current, prev, next
# current is 1, prev is none, and next is 2
# prev will become 2, current = 1 and next = none
# but we need to have change current to next before we change next.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

def reverse(head):
    prev = None
    curr = head
    while(curr):
        nxt = curr.next

        curr.next = prev
        prev = curr

        curr = nxt

    return prev

def printList (head):
    current = head
    while (current):
        print(current.val, " -> ")
        current = current.next
    print ("None")


node3 = ListNode(30)
node2 = ListNode(20, node3)
node1 = ListNode(10, node2)

head = node1

printList(head)

reversed = reverse(head)
printList(reversed)

